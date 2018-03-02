from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.apps import apps
from rest_framework import generics
from django.utils.translation import ugettext as _
from django.template import loader
from django.contrib.auth.decorators import login_required
from authority.forms import UserPermissionForm, GroupPermissionForm
from authority.models import Permission
from rest_framework.decorators import *
from rest_framework.renderers import *
from .serializers import PermissionSerializer
from django.contrib.auth.decorators import login_required
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)


class LoginRequiredMixin(object):

    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())


def get_next(request, obj=None):
    next = request.REQUEST.get('next')
    if not next:
        if obj and hasattr(obj, 'get_absolute_url'):
            next = obj.get_absolute_url()
        else:
            next = '/'
    return next


class PermissionAddAPIView(LoginRequiredMixin, CreateAPIView):

    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()

    def post(request, app_label, ssmodule_name, pk, approved=False, format=None):
        codename = request.POST.get('codename', None)
        try:
            model = apps.get_model(app_label, module_name)
        except LookupError:
            return permission_denied(request)
        obj = get_object_or_404(model, pk=pk)
        next = get_next(request, obj)
        if approved:
            if not request.user.has_perm('authority.add_permission'):
                return HttpResponseRedirect(
                    url_for_obj('authority-add-permission-request', obj))
            view_name = 'authority-add-permission'
        else:
            view_name = 'authority-add-permission-request'
        if request.method == 'POST':
            if codename is None:
                return HttpResponseForbidden(next)
            form = form_class(data=request.POST, obj=obj, approved=approved,
                              perm=codename, initial=dict(codename=codename))
            if not approved:
                # Limit permission request to current user
                form.data['user'] = request.user
            if form.is_valid():
                form.save(request)
                request.user.message_set.create(
                    message=_('You added a permission request.'))
                return HttpResponseRedirect(next)
        else:
            form = form_class(obj=obj, approved=approved, perm=codename,
                              initial=dict(codename=codename))
        context = {
            'form': form,
            'form_url': url_for_obj(view_name, obj),
            'next': next,
            'perm': codename,
            'approved': approved,
        }
        if extra_context:
            context.update(extra_context)
        return render_to_response(template_name, context, request)


class PermissionDetailAPIView(LoginRequiredMixin,
                              DestroyModelMixin,
                              UpdateModelMixin,
                              generics.RetrieveAPIView):

    def get_object(self, pk):
        try:
            return Permission.objects.get(pk=pk)
        except permission.DoesNotExist:
            raise Http404

    def approve_permission_request(request, permission_pk):
        requested_permission = get_object_or_404(Permission, pk=permission_pk)
        if request.user.has_perm('authority.approve_permission_requests'):
            requested_permission.approve(request.user)
            request.user.message_set.create(
                message=_('You approved the permission request.'))
        next = get_next(request, requested_permission)
        return HttpResponseRedirect(next)

    def delete_permission(request, permission_pk, approved):
        permission = get_object_or_404(Permission,  pk=permission_pk,
                                       approved=approved)
        if (request.user.has_perm('authority.delete_foreign_permissions') or
                request.user == permission.creator):
            permission.delete()
            if approved:
                msg = _('You removed the permission.')
            else:
                msg = _('You removed the permission request.')
            request.user.message_set.create(message=msg)
        next = get_next(request)
        return HttpResponseRedirect(next)

    """    def permission_denied(request, template_name=None, extra_context=None, message=None):

            if template_name is None:
                template_name = ('403.html', 'authority/403.html')
            context = {
                'request_path': request.url,
            }
            if extra_context:
                context.update(extra_context)
            return HttpResponseForbidden(loader.render_to_string(
                template_name=template_name,
                context=context,
                request=request,
            ))"""


class PermissionListAPIView(LoginRequiredMixin, ListAPIView):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()
