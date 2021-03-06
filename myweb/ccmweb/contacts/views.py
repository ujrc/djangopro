# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic.edit import DeleteView, CreateView, UpdateView

from accounts.views import account_detail
from accounts.models import Account
from .forms import ContactForm
from .models import Contact


@login_required
def contact_detail(request, uuid):
    contact = Contact.objects.get(uuid=uuid)
    return render(request,
                  'contacts/contact_detail.html', {'contact': contact})


@login_required
def contact_cru(request, uuid=None, account=None):
    if uuid:
        contact = get_object_or_404(Contact, uuid=uuid)
        if contact.owner != request.user:
            return HttpResponseForbidden()
    else:
        contact = Contact(owner=request.user)
    if request.POST:
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            # make sure the user owns the account
            account = form.cleaned_data['account']   
            if account.owner != request.user:
                return HttpResponseForbidden()
            # save the data
            # form.save()

            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            # return the user to the account detail view
            if request.is_ajax():
                return render(request,
                              'contacts/contact_item_view.html',
                              {'account': account, 'contact': contact}
                              )
            else:
                reverse_url = reverse(
                    'accounts.views.account_detail',
                    args=(account.uuid,)
                )
                return HttpResponseRedirect(reverse_url)
    else:
        form = ContactForm(instance=contact)

    if request.GET.get('account'):
        account = Account.objects.get(pk=request.GET.get('account'))

    variables = {
        'form': form,
        'contact': contact,
        'account': account
    }

    if request.is_ajax():
        template = 'contacts/contact_item_form.html'
    else:
        template = 'contacts/contact_cru.html'

    return render(request, template, variables)


class ContactMixin(object):
    model = Contact

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name': 'Contact'})
        return kwargs

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContactMixin, self).dispatch(*args, **kwargs)


class ContactDelete(ContactMixin, DeleteView):
    template_name = 'object_confirm_delete.html'

    def get_object(self, queryset=None):
        obj = super(ContactDelete, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        account = Account.objects.get(pk=obj.account.id)
        self.account = account
        return obj

    def get_success_url(self):
        return reverse(
            account_detail, args=(self.account.uuid))
