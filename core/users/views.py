from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm  # import your new form
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from .rag_utils import vectorstore 
from langchain.llms import HuggingFaceHub
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .rag_utils import vectorstore
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

from transformers import pipeline
from .rag_utils import vectorstore

qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

@csrf_exempt
def rag_chat_view(request):
    answer = None
    question=None
    if request.method == 'POST':
        question = request.POST.get('question')
        retriever = vectorstore.as_retriever()
        docs = retriever.get_relevant_documents(question)
        context = "\n".join([doc.page_content for doc in docs])

        result = qa_pipeline({
            "question": question,
            "context": context
        })
        answer = result['answer']

    return render(request, 'users/rag_chat.html', {"question": question, "answer": answer})


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "users/success.html")  # or redirect to login
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})
def custom_login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_doctor:
                return redirect("doctor_dashboard")
            elif user.is_patient:
                return redirect("patient_dashboard")
            else:
                return redirect("login")  # fallback for other types
        else:
            return render(request, "users/login.html", {"error": "Invalid credentials"})
    return render(request, "users/login.html")

@login_required
def patient_dashboard(request):
    return render(request, "users/patient_dashboard.html")

@login_required
def doctor_dashboard(request):
    return render(request, "users/doctor_dashboard.html")
def custom_logout_view(request):
    logout(request)
    return redirect("logged_out")

def logged_out(request):
    return render(request, "users/logged_out.html")

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required  # Ensure the user is logged in
def video_call(request, room_name):
    # Ensure the user is allowed to access this room (e.g., only patient and doctor can join)
    if request.user.is_authenticated:
        return render(request, "users/video_call.html", {"room_name": room_name})
    else:
        return redirect('login')
