import logging
import json
import random
import string
import io
from decouple import config
from PIL import Image, ImageDraw, ImageFont
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from app_core.forms import ScheduleForm
from app_core.models import Contact, Banner, About, Schedule, Skill, Counter, Service, SubService, WorkImage, Testimonial, \
    Partner, Faq, Privacy, SocialMedia, WorkVideo

# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
    contact = Contact.objects.all().last()
    banner = Banner.objects.all().last()
    about = About.objects.all().last()
    skills = Skill.objects.all().last()
    indicators = Counter.objects.all().last()
    servicios = Service.objects.all()
    works = WorkImage.objects.all().order_by('?')[:6]
    testimonials = Testimonial.objects.all().order_by('?')
    partners = Partner.objects.all().order_by('?')
    social_media = SocialMedia.objects.all()
    lunes_domingo = Schedule.objects.filter(days='04', activate=True).first()
    if lunes_domingo:
        schedules = [lunes_domingo]
    else:
        # Filtrar el resto de los horarios en caso de no encontrar "Monday-Sunday"
        schedules = Schedule.objects.filter(activate=True).exclude(days='04').order_by('days')
    context = {
        'contact': contact,
        'banner': banner,
        'about': about,
        'skills': skills,
        'indicators': indicators,
        'servicios': servicios,
        'works': works,
        'testimonials': testimonials,
        'partners': partners,
        'social_media': social_media,
        'schedules': schedules
    }

    if request.method == 'POST':
        if 'stay_connected' in request.POST:
            username = request.POST.get('userName')
            company = request.POST.get('companyName')
            email = request.POST.get('email')

            # y enviar el correo electrónico correspondiente
            send_msg_stay_connected(username, company, email)
            return render(request, 'app_core/pages/index.html', context)
    else:
        # Renderizar el template con ambos formularios
        return render(request, 'app_core/pages/index.html', context)


def about(request):
    banner = Banner.objects.all().last()
    contact = Contact.objects.all().last()
    about = About.objects.all().last()
    skills = Skill.objects.all().last()
    servicios = Service.objects.all()
    indicators = Counter.objects.all().last()
    testimonials = Testimonial.objects.all().order_by('?')
    social_media = SocialMedia.objects.all()
    works = WorkImage.objects.all().order_by('?')[:1]
    partners = Partner.objects.all().order_by('?')
    lunes_domingo = Schedule.objects.filter(days='04', activate=True).first()
    if lunes_domingo:
        schedules = [lunes_domingo]
    else:
        # Filtrar el resto de los horarios en caso de no encontrar "Monday-Sunday"
        schedules = Schedule.objects.filter(activate=True).exclude(days='04').order_by('days')
    context = {
        'contact': contact,
        'servicios': servicios,
        'about': about,
        'indicators': indicators,
        'skills': skills,
        'testimonials': testimonials,
        'partners': partners,
        'works': works,       
         'banner': banner,
        'social_media': social_media,
        'schedules': schedules
    }
    if request.method == 'POST':
        if 'stay_connected' in request.POST:
            username = request.POST.get('userName')
            company = request.POST.get('companyName')
            email = request.POST.get('email')

            # y enviar el correo electrónico correspondiente
            send_msg_stay_connected(username, company, email)
            return render(request, 'app_core/pages/about.html', context)
    else:
        # Renderizar el template con ambos formularios
        return render(request, 'app_core/pages/about.html', context)


def services(request):
    contact = Contact.objects.all().last()
    servicios = Service.objects.all()
    social_media = SocialMedia.objects.all()
    works = WorkImage.objects.all().order_by('?')[:1]    
    banner = Banner.objects.all().last()
    lunes_domingo = Schedule.objects.filter(days='04', activate=True).first()
    if lunes_domingo:
        schedules = [lunes_domingo]
    else:
        # Filtrar el resto de los horarios en caso de no encontrar "Monday-Sunday"
        schedules = Schedule.objects.filter(activate=True).exclude(days='04').order_by('days')

    context = {
        'contact': contact,
        'servicios': servicios,
        'works': works,        
        'banner': banner,
        'social_media': social_media,
        'schedules': schedules
    }
    if request.method == 'POST':
        if 'stay_connected' in request.POST:
            username = request.POST.get('userName')
            company = request.POST.get('companyName')
            email = request.POST.get('email')

            # y enviar el correo electrónico correspondiente
            send_msg_stay_connected(username, company, email)
            return render(request, 'app_core/pages/services.html', context)
    else:
        # Renderizar el template con ambos formularios
        return render(request, 'app_core/pages/services.html', context)


def services_view(request, slug):
    
    contact = Contact.objects.all().last()
    servicios = Service.objects.all()
    servicio = get_object_or_404(Service, slug=slug)
    subservicios = SubService.objects.filter(service=servicio)
    works = WorkImage.objects.all().order_by('?')[:1]
    partners = Partner.objects.all().order_by('?')
    social_media = SocialMedia.objects.all()
    about = About.objects.all().last()    
    banner = Banner.objects.all().last()
    lunes_domingo = Schedule.objects.filter(days='04', activate=True).first()
    if lunes_domingo:
        schedules = [lunes_domingo]
    else:
        # Filtrar el resto de los horarios en caso de no encontrar "Monday-Sunday"
        schedules = Schedule.objects.filter(activate=True).exclude(days='04').order_by('days')

    context = {
        'contact': contact,
        'banner': banner,
        'servicio': servicio,
        'servicios': servicios,
        'subservicios': subservicios,
        'works': works,
        'partners': partners,
        'social_media': social_media,
        'about': about,
        'schedules': schedules
    }
    if request.method == 'POST':
        if 'stay_connected' in request.POST:
            username = request.POST.get('userName')
            company = request.POST.get('companyName')
            email = request.POST.get('email')

            # y enviar el correo electrónico correspondiente
            send_msg_stay_connected(username, company, email)
            return render(request, 'app_core/pages/service.html', context)
    else:
        # Renderizar el template con ambos formularios
        return render(request, 'app_core/pages/service.html', context)


def works(request):
    contact = Contact.objects.all().last()
    servicios = Service.objects.all()
    gallery = WorkImage.objects.all().order_by('?')
    social_media = SocialMedia.objects.all()
    about = About.objects.all().last()
    partners = Partner.objects.all().order_by('?')
    banner = Banner.objects.all().last()
    lunes_domingo = Schedule.objects.filter(days='04', activate=True).first()
    if lunes_domingo:
        schedules = [lunes_domingo]
    else:
        # Filtrar el resto de los horarios en caso de no encontrar "Monday-Sunday"
        schedules = Schedule.objects.filter(activate=True).exclude(days='04').order_by('days')

    context = {
        'contact': contact,
        'servicios': servicios,
        'works': gallery,
        'about': about,
        'banner': banner,
        'partners': partners,
        'social_media': social_media,
        'schedules': schedules
    }
    if request.method == 'POST':
        if 'stay_connected' in request.POST:
            username = request.POST.get('userName')
            company = request.POST.get('companyName')
            email = request.POST.get('email')

            # y enviar el correo electrónico correspondiente
            send_msg_stay_connected(username, company, email)
            return render(request, 'app_core/pages/works.html', context)
    else:
        # Renderizar el template con ambos formularios
        return render(request, 'app_core/pages/works.html', context)


def works_videos(request):
    contact = Contact.objects.all().last()
    servicios = Service.objects.all()
    gallery = WorkImage.objects.all().order_by('?')[:6]
    social_media = SocialMedia.objects.all()
    about = About.objects.all().last()
    partners = Partner.objects.all().order_by('?')
    banner = Banner.objects.all().last()
    videos = WorkVideo.objects.all()
    testimonials = Testimonial.objects.all().order_by('?')
    lunes_domingo = Schedule.objects.filter(days='04', activate=True).first()
    if lunes_domingo:
        schedules = [lunes_domingo]
    else:
        # Filtrar el resto de los horarios en caso de no encontrar "Monday-Sunday"
        schedules = Schedule.objects.filter(activate=True).exclude(days='04').order_by('days')
    context = {
        'contact': contact,
        'servicios': servicios,
        'works': gallery,
        'about': about,
        'partners': partners,
        'banner': banner,
        'social_media': social_media,
        'videos': videos,
        'testimonials': testimonials,
        'schedules': schedules
    }
    if request.method == 'POST':
        if 'stay_connected' in request.POST:
            username = request.POST.get('userName')
            company = request.POST.get('companyName')
            email = request.POST.get('email')

            # y enviar el correo electrónico correspondiente
            send_msg_stay_connected(username, company, email)
            return render(request, 'app_core/pages/works_videos.html', context)
    else:
        # Renderizar el template con ambos formularios
        return render(request, 'app_core/pages/works_videos.html', context)


def faq(request):
    contact = Contact.objects.all().last()
    faqs = Faq.objects.all()
    testimonials = Testimonial.objects.all().order_by('?')
    servicios = Service.objects.all()
    works = WorkImage.objects.all().order_by('?')[:1]
    social_media = SocialMedia.objects.all()
    partners = Partner.objects.all().order_by('?')
    about = About.objects.all().last()    
    banner = Banner.objects.all().last()
    lunes_domingo = Schedule.objects.filter(days='04', activate=True).first()
    if lunes_domingo:
        schedules = [lunes_domingo]
    else:
        # Filtrar el resto de los horarios en caso de no encontrar "Monday-Sunday"
        schedules = Schedule.objects.filter(activate=True).exclude(days='04').order_by('days')

    context = {
        'contact': contact,
        'servicios': servicios,
        'faqs': faqs,
        'social_media': social_media,
        'partners': partners,
        'works': works,
        'about': about,
        'banner': banner,
        'testimonials': testimonials,
        'schedules': schedules

    }
    if request.method == 'POST':
        if 'stay_connected' in request.POST:
            username = request.POST.get('userName')
            company = request.POST.get('companyName')
            email = request.POST.get('email')

            # y enviar el correo electrónico correspondiente
            send_msg_stay_connected(username, company, email)
            return render(request, 'app_core/pages/faq.html', context)
    else:
        # Renderizar el template con ambos formularios
        return render(request, 'app_core/pages/faq.html', context)


def contact(request):
    contact = Contact.objects.all().last()
    servicios = Service.objects.all()
    testimonials = Testimonial.objects.all().order_by('?')
    social_media = SocialMedia.objects.all()
    works = WorkImage.objects.all().order_by('?')[:1]
    about = About.objects.all().last()
    partners = Partner.objects.all().order_by('?')    
    banner = Banner.objects.all().last()
    lunes_domingo = Schedule.objects.filter(days='04', activate=True).first()
    if lunes_domingo:
        schedules = [lunes_domingo]
    else:
        # Filtrar el resto de los horarios en caso de no encontrar "Monday-Sunday"
        schedules = Schedule.objects.filter(activate=True).exclude(days='04').order_by('days')

    context = {
        'banner': banner,
        'servicios': servicios,
        'contact': contact,
        'about': about,
        'testimonials': testimonials,
        'social_media': social_media,
        'partners': partners,
        'works': works,
        'schedules': schedules
    }
    if request.method == 'POST':
        data = json.loads(request.body)
        # Ahora puedes acceder a los datos como un diccionario Python
        user_captcha = data.get('captcha')
        username = data.get('userName')
        email = data.get('userEmail')
        phone = data.get('userPhone')
        # subject = data.get('userSubject')
        message = data.get('userMessage')
        tipo_formulario = data.get('form_identifier')
        correct_captcha = request.session.get('captcha_text', '')
        try:
            if tipo_formulario == 'stay_connected':
                email = request.POST.get('email')
                # y enviar el correo electrónico correspondiente
                send_msg_stay_connected(email)
                return render(request, 'app_core/pages/contact.html', context)

            elif tipo_formulario == 'contact_us_form':
                # Decodificar la carga útil JSON de la solicitud
                if user_captcha == correct_captcha:
                    data = {
                        'mensaje': 'El mensaje ha sido enviado correctamente.',
                        'resultado': True,
                    }

                    # y enviar el correo electrónico correspondiente
                    send_msg_contact_us(username, email, phone, message)
                    return JsonResponse(data)

                else:
                    data = {
                        'mensaje': 'El captcha no coincide',
                        'resultado': False,
                    }
                    return JsonResponse(data)
            else:
                print("No reconoce el name de los botones")

        except json.JSONDecodeError:
            print('Sera q esta entrando aqui?')
            # Manejar errores de decodificación JSON
            return JsonResponse({'mensaje': 'Error en la carga útil JSON'}, status=400)

    else:
        # Renderizar el template con ambos formularios
        return render(request, 'app_core/pages/contact.html', context)


def privacy(request):
    banner = Banner.objects.all().last()
    contact = Contact.objects.all().last()
    servicios = Service.objects.all()
    privacy = Privacy.objects.all().last()
    social_media = SocialMedia.objects.all()
    partners = Partner.objects.all().order_by('?')
    works = WorkImage.objects.all().order_by('?')[:1]
    about = About.objects.all().last()
    lunes_domingo = Schedule.objects.filter(days='04', activate=True).first()
    if lunes_domingo:
        schedules = [lunes_domingo]
    else:
        # Filtrar el resto de los horarios en caso de no encontrar "Monday-Sunday"
        schedules = Schedule.objects.filter(activate=True).exclude(days='04').order_by('days')
    context = {
        'contact': contact,
        'servicios': servicios,
        'privacy': privacy,
        'social_media': social_media,
        'partners': partners,
        'works': works,
        'about': about,
        'banner': banner,
        'schedules': schedules

    }
    if request.method == 'POST':
        if 'stay_connected' in request.POST:
            username = request.POST.get('userName')
            company = request.POST.get('companyName')
            email = request.POST.get('email')

            # y enviar el correo electrónico correspondiente
            send_msg_stay_connected(username, company, email)
            return render(request, 'app_core/pages/privacy.html', context)
    else:
        # Renderizar el template con ambos formularios
        return render(request, 'app_core/pages/privacy.html', context)


def generate_captcha():
    width, height = 140, 50
    captcha_image = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(captcha_image)

    # Fuente para el texto del CAPTCHA
    font = ImageFont.load_default(30)  # Usa una fuente predeterminada

    # Generar texto CAPTCHA
    captcha_text = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

    # Dibujar el texto en la imagen
    draw.text((10, 10), captcha_text, fill=(0, 0, 0), font=font)

    return captcha_text, captcha_image


def captcha_image(request):
    captcha_text, captcha_image = generate_captcha()

    # Guardar la imagen en un buffer de memoria
    image_buffer = io.BytesIO()
    captcha_image.save(image_buffer, format='PNG')
    image_buffer.seek(0)

    # Guardar el texto CAPTCHA en la variable de sesión de Django
    request.session['captcha_text'] = captcha_text

    # Devolver la imagen como una respuesta HTTP
    return HttpResponse(image_buffer, content_type='image/png')


def send_msg_stay_connected(username, company, email):
    contact = Contact.objects.all().last()
    email_contact = contact.email
    about = About.objects.all().last()
    company_name = about.company_name
    subject = f'Stay Connected {company_name}'
    message = f'Hello, {company_name} you have a new subscriber: \nEmail: {email}.'
    from_email = config('EMAIL_HOST_USER')
    recipient_list = [email_contact]
    send_mail(subject, message, from_email, recipient_list)


def send_msg_contact_us(username, email, phone, get_message):
    contact = Contact.objects.all().last()
    email_contact = contact.email
    about = About.objects.all().last()
    company_name = about.company_name
    subject = f'You got a contact message from {company_name} website'
    message = f'Hello {company_name}! you got a contact message from website: \n\nName: {username} \nEmail: {email} \nPhone: {phone} \n\nMessage: {get_message}'
    from_email = config('EMAIL_HOST_USER')
    recipient_list = [email_contact]
    send_mail(subject, message, from_email, recipient_list)


def mail_view(request):
    return HttpResponseRedirect(
        'https://accounts.zoho.com/signin?servicename=VirtualOffice&signupurl=https://www.zoho.com/workplace/pricing.html/')

def follow_us(request):
    contact = Contact.objects.all().last()
    social_media = SocialMedia.objects.all()
    works_footer = WorkImage.objects.all().order_by('?')[:2]
    servicios = Service.objects.all()
    about = About.objects.all().last()
    context = {
        'contact': contact,
        'social_media': social_media,
        'works_footer': works_footer,
        'servicios': servicios,
        'about': about
    }
    return render(request, 'app_info/base.html', context)

def crear_horario(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a la vista de mostrar horarios después de guardar
            print("Formulario válido")
            return redirect('app_core:mostrar_horarios')  
        else:
            print("Errores en el formulario:", form.errors) 
            return render(request, 'app_core/pages/form.html', {'form': form})
    else:
        form = ScheduleForm()

    # Solo mostrar el formulario de creación
    return render(request, 'app_core/pages/form.html', {'form': form})
def mostrar_horarios(request):
    # Intentar encontrar el horario "Monday-Sunday"
    lunes_domingo = Schedule.objects.filter(days='04', activate=True).first()
    if lunes_domingo:
        schedules = [lunes_domingo]
    else:
        # Filtrar el resto de los horarios en caso de no encontrar "Monday-Sunday"
        schedules = Schedule.objects.filter(activate=True).exclude(days='04').order_by('days')

    context = {
        'schedules': schedules
    }
    return render(request, 'app_core/pages/mostrar_horarios.html', context)

def handler_404(request, exception):
    path = request.path
    
    if path.startswith('/info/'):
        redirect_url = '/info/'  
    elif path.startswith('/administrator/'):
        redirect_url = '/administrator/index' 
    else:
        redirect_url = '/'  
    return render(request, 'app_core/pages/404.html',{'redirect_url': redirect_url}, status=404)


def custom_500(request):
    contact = Contact.objects.all().last()

    return render(request, 'app_core/pages/500.html',{'contact': contact}, status=500)
