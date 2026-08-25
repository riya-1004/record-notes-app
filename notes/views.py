from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm, EmailSignUpForm


def signup(request):
    """Simple sign-up page — just email + password, no username field."""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = EmailSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome! Your account was created.')
            return redirect('home')
    else:
        form = EmailSignUpForm()

    return render(request, 'notes/signup.html', {'form': form})


@login_required
def home(request):
    """Show the note form and the list of the logged-in user's notes."""
    form = NoteForm()
    notes = Note.objects.filter(owner=request.user)
    context = {
        'form': form,
        'notes': notes,
        'note_count': notes.count(),
    }
    return render(request, 'notes/home.html', context)


@login_required
def create_note(request):
    """Handle note creation and show a dedicated 'note saved' confirmation page."""
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            if note.content.strip():
                note.owner = request.user
                note.save()
                return render(request, 'notes/note_saved.html', {'note': note})
            else:
                messages.error(request, 'Please write something before saving.')
        else:
            messages.error(request, 'Please write something before saving.')
        return redirect('home')

    return redirect('home')


@login_required
def update_note(request, note_id):
    """Edit an existing note that belongs to the logged-in user."""
    note = get_object_or_404(Note, id=note_id, owner=request.user)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            edited_note = form.save(commit=False)
            if edited_note.content.strip():
                edited_note.save()
                messages.success(request, 'Note updated successfully!')
                return redirect('home')
            else:
                messages.error(request, 'Please write something before saving.')
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/edit_note.html', {'form': form, 'note': note})


@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, owner=request.user)
    note.delete()
    messages.success(request, 'Note deleted successfully!')
    return redirect('home')