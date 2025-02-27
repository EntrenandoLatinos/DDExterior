import os
import gc
import logging
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from io import BytesIO
from django.shortcuts import render, redirect, get_object_or_404
from selenium import webdriver
from django.contrib import messages
from django.core.files import File
from PIL import Image
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from app_core.forms import ContactForm, BannerForm, AboutForm, ScheduleForm, SkillForm, CounterForm, ServiceForm, ServiceDeleteForm, \
    SubServiceForm, TestimonialForm, TestimonialDeleteForm, PartnerForm, FaqForm, PrivacyForm, WorkForm, \
    SocialMediaForm, WorkVideoForm, TeamPersonForm
from app_core.models import Contact, Banner, About, Schedule, Skill, Counter, Service, SubService, WorkImage, Testimonial, \
    Partner, Faq, Privacy, SocialMedia, WorkVideo, TeamPerson


logger = logging.getLogger(__name__)


def login_redirect(request):
    if request.user.is_superuser:
        return redirect('app_user:admin_index')


def data_company():
    about = About.objects.all().last()
    company_name = about.company_name if about and about.company_name else ''
    company_name_first_letter = company_name[0].upper() if company_name and about.company_name else ''
    is_gallery = about.is_gallery if about else False
    is_team = about.is_team if about else False

    context = {
        'company_name': company_name,
        'company_name_first_letter': company_name_first_letter,
        'is_gallery': is_gallery,
        'is_team': is_team
    }
    return context


@login_required
def admin_index(request):
    company_data = data_company()
    context = {
        'company_data': company_data
    }
    return render(request, 'app_user/pages/index.html', context)


############### CONTACT INFO ###############
@login_required
def contact_update(request):
    company_data = data_company()
    about = About.objects.all().last()
    company_name = about.company_name if about and about.company_name else ''
    company_name_first_letter = company_name[0].upper() if company_name and about.company_name else ''
    contact = Contact.objects.all().last()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST, request.FILES, instance=contact)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('app_user:admin_index')
    else:
        contact_form = ContactForm(instance=contact)

    context = {
        'company_data': company_data,
        'contact': contact,
        'contact_form': contact_form,
        'company_name': company_name,
        'company_name_first_letter': company_name_first_letter
    }
    return render(request, 'app_user/pages/contact.html', context)


############### BANNER ###############
@login_required
def banner_update(request):
    company_data = data_company()
    banner = Banner.objects.all().last()

    if request.method == 'POST':
        banner_form = BannerForm(request.POST, request.FILES, instance=banner)
        if banner_form.is_valid():
            banner_form.save()
            return redirect('app_user:admin_index')
    else:
        banner_form = BannerForm(instance=banner)

    context = {'company_data': company_data, 'banner': banner, 'banner_form': banner_form}
    return render(request, 'app_user/pages/banner.html', context)


############### ABOUT ###############
@login_required
def about_update(request):
    company_data = data_company()
    about = About.objects.all().last()

    if request.method == 'POST':
        about_form = AboutForm(request.POST, request.FILES, instance=about)
        if about_form.is_valid():
            about_form.save()
            return redirect('app_user:admin_index')
    else:
        about_form = AboutForm(instance=about)

    context = {'company_data': company_data, 'about': about, 'about_form': about_form}
    return render(request, 'app_user/pages/about.html', context)


############### WHY US ###############
@login_required
def skill_update(request):
    company_data = data_company()
    skill = Skill.objects.all().last()

    if request.method == 'POST':
        skill_form = SkillForm(request.POST, request.FILES, instance=skill)
        if skill_form.is_valid():
            skill_form.save()
            return redirect('app_user:admin_index')
    else:
        skill_form = SkillForm(instance=skill)

    context = {'company_data': company_data, 'skill': skill, 'skill_form': skill_form}
    return render(request, 'app_user/pages/skill.html', context)


############### COUNTERS ###############
@login_required
def counter_update(request):
    company_data = data_company()
    counter = Counter.objects.all().last()

    if request.method == 'POST':
        counter_form = CounterForm(request.POST, request.FILES, instance=counter)
        if counter_form.is_valid():
            counter_form.save()
            return redirect('app_user:admin_index')
    else:
        counter_form = CounterForm(instance=counter)

    context = {'company_data': company_data, 'counter': counter, 'counter_form': counter_form}
    return render(request, 'app_user/pages/counter.html', context)


############### SERVICES ###############
@login_required
def services(request):
    company_data = data_company()
    services = Service.objects.all()
    context = {'company_data': company_data, 'services': services}
    return render(request, 'app_user/pages/services.html', context)


@login_required
def service_create(request):
    company_data = data_company()
    if request.method == 'POST':
        service_form = ServiceForm(request.POST, request.FILES)
        if service_form.is_valid():
            new_service = service_form.save()
            return redirect('app_user:services')
    else:
        service_form = ServiceForm()

    return render(request, 'app_user/pages/service_create.html',
                  {'company_data': company_data, 'service_form': service_form})


@login_required
def service_update(request, pk):
    company_data = data_company()
    service = get_object_or_404(Service, id=pk)

    if request.method == 'POST':
        if 'update_service' in request.POST:
            service_form = ServiceForm(request.POST, request.FILES, instance=service, prefix='service_update')
            if service_form.is_valid():
                print("Almenos esntramos aqui")
                service_form.save()
                return redirect('app_user:services')
        elif 'delete_service' in request.POST:
            service_delete_form = ServiceDeleteForm(request.POST, prefix='service_delete', initial={'id_to_delete': pk})
            if service_delete_form.is_valid():
                id_to_delete = service_delete_form.cleaned_data['id_to_delete']
                # Eliminar el registro con el id especificado
                Service.objects.filter(id=id_to_delete).delete()
                return redirect('app_user:services')
    else:
        service_form = ServiceForm(instance=service, prefix='service_update')
        service_delete_form = ServiceDeleteForm(prefix='service_delete', initial={'id_to_delete': pk})

    context = {'company_data': company_data, 'service': service, 'service_form': service_form,
               'service_delete_form': service_delete_form}
    return render(request, 'app_user/pages/service_update.html', context)


############### SUBSERVICES ###############
@login_required
def subservices(request, pk):
    company_data = data_company()
    service = get_object_or_404(Service, id=pk)
    subservices = SubService.objects.filter(service=pk)

    if request.method == 'POST':
        subservice_id = request.POST.get('deleteSubserviceInput', '')
        SubService.objects.filter(pk=subservice_id).delete()

    context = {'company_data': company_data, 'subservices': subservices, 'service': service}
    return render(request, 'app_user/pages/subservices.html', context)


@login_required
def subservice_create(request, pk):
    company_data = data_company()
    service = get_object_or_404(Service, id=pk)
    subservices = SubService.objects.filter(service=pk)

    if request.method == 'POST':
        subservice_form = SubServiceForm(request.POST, request.FILES)
        if subservice_form.is_valid():
            new_subservice = subservice_form.save()
            context = {'service': service, 'subservices': subservices}
            return redirect(reverse('app_user:subservices', args=[service.id]), context)
    else:
        subservice_form = SubServiceForm()
        context = {'company_data': company_data, 'service': service, 'subservice_form': subservice_form}

    return render(request, 'app_user/pages/subservice_create.html', context)


@login_required
def subservice_update(request, pk):
    company_data = data_company()
    subservice = get_object_or_404(SubService, id=pk)
    service = get_object_or_404(Service, service_subservice__id=pk)
    subservices = SubService.objects.filter(service=service.id)

    if request.method == 'POST':
        subservice_form = SubServiceForm(request.POST, request.FILES, instance=subservice)
        if subservice_form.is_valid():
            subservice_form.save()
            context = {'service': service, 'subservices': subservices}
            return redirect(reverse('app_user:subservices', args=[service.id]), context)

    else:
        subservice_form = SubServiceForm(instance=subservice)

    context = {'company_data': company_data, 'service': service, 'subservice': subservice,
               'subservice_form': subservice_form}
    return render(request, 'app_user/pages/subservice_update.html', context)


################# REVIEWS ##################
@login_required
def reviews_index(request):
    company_data = data_company()
    context = {'company_data': company_data}
    return render(request, 'app_user/pages/reviews_index.html', context)


############# GOOGLE BUSINESS ##############
def assign_letter(name):
    # Obtener la primera letra del nombre
    first_letter = name[0].lower() if name else None

    # Construir la ruta de la imagen basada en la primera letra del nombre
    if first_letter and first_letter.isalpha() and first_letter.isascii():
        image_filename = f'{first_letter}.webp'
        image_folder = settings.STATIC_ROOT + 'app_user/images/abecedario/'
        # Obtén la ruta del archivo de la imagen
        FILE_PATH = f'{image_folder}{image_filename}'
        # Abre el archivo localmente
        local_file = open(FILE_PATH, "rb")
        # Crea un objeto File de Django
        imageFile = File(local_file)

        img_letter_name = {
            'image_filename':image_filename,
            'imageFile':imageFile
        }
        return img_letter_name
    

def ensure_trailing_slash(url):
    # Verifica si la URL termina con '/'
    if not url.endswith('/'):
        # Si no termina con '/', añade '/'
        url += '/'
    return url
    

@login_required
def google_business(request):
    company_data = data_company()
    testimonials = Testimonial.objects.exclude(url__isnull=True)
    if 'delete_testimonial' in request.POST:
        testimonial_delete_form = TestimonialDeleteForm(request.POST)
        if testimonial_delete_form.is_valid():
            id_to_delete = testimonial_delete_form.cleaned_data['id_to_delete']
            # Eliminar el registro con el id especificado
            Testimonial.objects.filter(id=id_to_delete).delete()
            return redirect('app_user:google_business')

    context = {'company_data': company_data, 'testimonials': testimonials}
    return render(request, 'app_user/pages/google_business.html', context)


@login_required
def google_business_create(request):
    company_data = data_company()
    if request.method == 'POST':
        testimonial_form = TestimonialForm(request.POST, request.FILES)
        if testimonial_form.is_valid():
            url_google_business_get = testimonial_form.cleaned_data['url']
            url_google_business = ensure_trailing_slash(url_google_business_get)

            if url_google_business:
                ############ ESTO ES PARA PRUEBAS LOCALES ############
                # base_dir = settings.BASE_DIR
                # chromedriver_rel_path = os.path.join(base_dir, 'static', 'chromedriver', 'chromedriver')
                ############ ESTO ES PARA PRUEBAS LOCALES ############

                chromedriver_rel_path = '/snap/bin/chromium.chromedriver'
                logger.debug(f'Este es el path de chromedriver: {chromedriver_rel_path}')

                chrome_options = Options()
                chrome_options.add_argument("--no-sandbox")
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--disable-dev-shm-usage")
                chrome_options.add_argument('--disable-gpu')
                chrome_options.add_argument('--disable-software-rasterizer')
                chrome_options.add_argument('--disable-extensions')
                chrome_service = ChromeService(executable_path=chromedriver_rel_path)
                driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

                try:
                    logger.debug(f'Esta es la url: {url_google_business}')
                    driver.get(url_google_business)
                    timeout = 10  # Ajusta este valor según sea necesario
                    espera = WebDriverWait(driver, timeout)
                    # Nombre del q hace el rivew
                    name = driver.find_element(By.CLASS_NAME, 'sZ0S5')
                    nombre = name.text
                    # Puntuacion - Estrellas
                    stars = driver.find_element(By.CLASS_NAME, 'kvMYJc')
                    aria_label = stars.get_attribute('aria-label')
                    # Extraer el número de estrellas del valor de aria-label
                    num_estrellas = int(aria_label.split()[0])
                    # Esperar hasta que el botón sea clickeable
                    try:
                        button = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.CLASS_NAME, "kyuRq"))
                        )
                        # Hacer clic en el botón
                        button.click()
                        logger.debug("Se hizo clic en el botón con éxito.")
                    except:
                        logger.debug("No se pudo hacer clic en el botón.")
                    # Comentario
                    comment = driver.find_element(By.CLASS_NAME, 'wiI7pd')
                    comentario = comment.text

                    # Modificar los datos del formulario antes de guardar
                    testimonial = testimonial_form.save(commit=False)
                    testimonial.name = nombre
                    testimonial.stars = num_estrellas
                    testimonial.description = comentario
                    img_letter_name = assign_letter(nombre)
                    image_filename = img_letter_name['image_filename']
                    imageFile = img_letter_name['imageFile']
                    if image_filename and imageFile:
                        # Guarda la imagen en el campo 'image' de la instancia del modelo
                        testimonial.image.save(image_filename, imageFile)
                    testimonial.save()

                finally:
                    # Cierra el navegador
                    driver.quit()
                    chrome_service.stop()
                    gc.collect()

            messages.success(request, 'Testimonio guardado exitosamente.')
            return redirect('app_user:google_business')
    else:
        testimonial_form = TestimonialForm()

    return render(request, 'app_user/pages/google_business_create.html',
                  {'company_data': company_data, 'testimonial_form': testimonial_form})


@login_required
def google_business_update(request, pk):
    company_data = data_company()
    testimonial = get_object_or_404(Testimonial, id=pk)

    if request.method == 'POST':
        if 'update_testimonial' in request.POST:
            testimonial_form = TestimonialForm(request.POST, request.FILES, instance=testimonial,
                                               prefix='testimonial_update')

            if testimonial_form.is_valid():
                url_google_business_get = testimonial_form.cleaned_data['url']
                url_google_business = ensure_trailing_slash(url_google_business_get)

                if url_google_business:
                    ############ ESTO ES PARA PRUEBAS LOCALES ############
                    # base_dir = settings.BASE_DIR
                    # chromedriver_rel_path = os.path.join(base_dir, 'static', 'chromedriver', 'chromedriver')
                    ############ ESTO ES PARA PRUEBAS LOCALES ############

                    chromedriver_rel_path = '/snap/bin/chromium.chromedriver'
                    logger.debug(f'Este es el path de chromedriver: {chromedriver_rel_path}')

                    chrome_options = Options()
                    chrome_options.add_argument("--no-sandbox")
                    chrome_options.add_argument("--headless")
                    chrome_options.add_argument("--disable-dev-shm-usage")
                    chrome_options.add_argument('--disable-gpu')
                    chrome_options.add_argument('--disable-software-rasterizer')
                    chrome_options.add_argument('--disable-extensions')
                    chrome_service = ChromeService(executable_path=chromedriver_rel_path)
                    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

                    try:
                        logger.debug(f'Esta es la url: {url_google_business}')
                        driver.get(url_google_business)
                        timeout = 10  # Ajusta este valor según sea necesario
                        espera = WebDriverWait(driver, timeout)
                        # Nombre del q hace el rivew
                        name = driver.find_element(By.CLASS_NAME, 'sZ0S5')
                        nombre = name.text
                        # Puntuacion - Estrellas
                        stars = driver.find_element(By.CLASS_NAME, 'kvMYJc')
                        aria_label = stars.get_attribute('aria-label')
                        # Extraer el número de estrellas del valor de aria-label
                        num_estrellas = int(aria_label.split()[0])
                        # Esperar hasta que el botón sea clickeable
                        try:
                            button = WebDriverWait(driver, 10).until(
                                EC.element_to_be_clickable((By.CLASS_NAME, "kyuRq"))
                            )
                            # Hacer clic en el botón
                            button.click()
                            logger.debug("Se hizo clic en el botón con éxito.")
                        except:
                            logger.debug("No se pudo hacer clic en el botón.")
                        # Comentario
                        comment = driver.find_element(By.CLASS_NAME, 'wiI7pd')
                        comentario = comment.text

                        # Modificar los datos del formulario antes de guardar
                        testimonial = testimonial_form.save(commit=False)
                        testimonial.name = nombre
                        testimonial.stars = num_estrellas
                        testimonial.description = comentario
                        img_letter_name = assign_letter(nombre)
                        image_filename = img_letter_name['image_filename']
                        imageFile = img_letter_name['imageFile']
                        if image_filename and imageFile:
                            # Guarda la imagen en el campo 'image' de la instancia del modelo
                            testimonial.image.save(image_filename, imageFile)
                        testimonial.save()

                    finally:
                        # Cierra el navegador
                        driver.quit()
                        chrome_service.stop()
                        gc.collect()

                messages.success(request, 'Testimonio guardado exitosamente.')
                return redirect('app_user:google_business')

        elif 'delete_testimonial' in request.POST:
            testimonial_delete_form = TestimonialDeleteForm(request.POST, prefix='testimonial_delete',
                                                            initial={'id_to_delete': pk})
            if testimonial_delete_form.is_valid():
                id_to_delete = testimonial_delete_form.cleaned_data['id_to_delete']
                # Eliminar el registro con el id especificado
                Testimonial.objects.filter(id=id_to_delete).delete()
                return redirect('app_user:google_business')
    else:
        testimonial_form = TestimonialForm(instance=testimonial, prefix='testimonial_update')
        testimonial_delete_form = TestimonialDeleteForm(prefix='testimonial_delete', initial={'id_to_delete': pk})

    context = {'company_data': company_data, 'testimonial': testimonial, 'testimonial_form': testimonial_form,
               'testimonial_delete_form': testimonial_delete_form}
    return render(request, 'app_user/pages/google_business_update.html', context)


############### TESTIMONIALS ###############
@login_required
def testimonials(request):
    company_data = data_company()
    testimonials = Testimonial.objects.exclude(url__isnull=False)
    context = {'company_data': company_data, 'testimonials': testimonials}
    return render(request, 'app_user/pages/testimonials.html', context)

@login_required
def testimonials_create(request):
    company_data = data_company()
    if request.method == 'POST':
        testimonial_form = TestimonialForm(request.POST, request.FILES)
        if testimonial_form.is_valid():
            # Obtener el nombre del campo 'name' del formulario
            name = testimonial_form.cleaned_data.get('name')
            # Guardar el testimonio
            testimonial = testimonial_form.save(commit=False)
            img_letter_name = assign_letter(name)
            image_filename = img_letter_name['image_filename']
            imageFile = img_letter_name['imageFile']
            if image_filename and imageFile:
                # Guarda la imagen en el campo 'image' de la instancia del modelo
                testimonial.image.save(image_filename, imageFile)
                testimonial.save()
            return redirect('app_user:testimonials')
    else:
        testimonial_form = TestimonialForm()

    return render(request, 'app_user/pages/testimonials_create.html',
                  {'company_data': company_data, 'testimonial_form': testimonial_form})


@login_required
def testimonial_update(request, pk):
    company_data = data_company()
    testimonial = get_object_or_404(Testimonial, id=pk)

    if request.method == 'POST':
        if 'update_testimonial' in request.POST:
            testimonial_form = TestimonialForm(request.POST, request.FILES, instance=testimonial,
                                               prefix='testimonial_update')

            if testimonial_form.is_valid():
                # Obtener el nombre del campo 'name' del formulario
                name = testimonial_form.cleaned_data.get('name')
                # Guardar el testimonio
                testimonial = testimonial_form.save(commit=False)
                img_letter_name = assign_letter(name)
                image_filename = img_letter_name['image_filename']
                imageFile = img_letter_name['imageFile']
                if image_filename and imageFile:
                    # Guarda la imagen en el campo 'image' de la instancia del modelo
                    testimonial.image.save(image_filename, imageFile)
                    testimonial.save()
                return redirect('app_user:testimonials')

        elif 'delete_testimonial' in request.POST:
            testimonial_delete_form = TestimonialDeleteForm(request.POST, prefix='testimonial_delete',
                                                            initial={'id_to_delete': pk})
            if testimonial_delete_form.is_valid():
                id_to_delete = testimonial_delete_form.cleaned_data['id_to_delete']
                # Eliminar el registro con el id especificado
                Testimonial.objects.filter(id=id_to_delete).delete()
                return redirect('app_user:testimonials')
    else:
        testimonial_form = TestimonialForm(instance=testimonial, prefix='testimonial_update')
        testimonial_delete_form = TestimonialDeleteForm(prefix='testimonial_delete', initial={'id_to_delete': pk})

    context = {
        'company_data': company_data,
        'testimonial': testimonial,
        'testimonial_form': testimonial_form,
        'testimonial_delete_form': testimonial_delete_form
    }
    return render(request, 'app_user/pages/testimonial_update.html', context)


############### PARTNERS ###############
@login_required
def partners(request):
    company_data = data_company()
    partners = Partner.objects.all()

    if request.method == 'POST':
        partner_id = request.POST.get('deletePartnerInput', '')
        Partner.objects.filter(pk=partner_id).delete()

    context = {'company_data': company_data, 'partners': partners}
    return render(request, 'app_user/pages/partners.html', context)


@login_required
def partner_create(request):
    company_data = data_company()
    if request.method == 'POST':
        partner_form = PartnerForm(request.POST, request.FILES)
        if partner_form.is_valid():
            new_partner = partner_form.save()
            return redirect('app_user:partners')
    else:
        partner_form = PartnerForm()

    return render(request, 'app_user/pages/partner_create.html',
                  {'company_data': company_data, 'partner_form': partner_form})


@login_required
def partner_update(request, pk):
    company_data = data_company()
    partner = get_object_or_404(Partner, id=pk)

    if request.method == 'POST':
        partner_form = PartnerForm(request.POST, request.FILES, instance=partner)
        if partner_form.is_valid():
            partner_form.save()
            return redirect('app_user:partners')

    else:
        partner_form = PartnerForm(instance=partner)

    context = {'company_data': company_data, 'partner': partner, 'partner_form': partner_form}
    return render(request, 'app_user/pages/partner_update.html', context)


############### FAQ´s ###############
@login_required
def faqs(request):
    company_data = data_company()
    faqs = Faq.objects.all()

    if request.method == 'POST':
        faq_id = request.POST.get('deleteFaqInput', '')
        Faq.objects.filter(pk=faq_id).delete()

    context = {'company_data': company_data, 'faqs': faqs}
    return render(request, 'app_user/pages/faqs.html', context)


@login_required
def faq_create(request):
    company_data = data_company()
    if request.method == 'POST':
        faq_form = FaqForm(request.POST, request.FILES)
        if faq_form.is_valid():
            new_faq = faq_form.save()
            return redirect('app_user:faqs')
    else:
        faq_form = FaqForm()

    return render(request, 'app_user/pages/faq_create.html', {'company_data': company_data, 'faq_form': faq_form})


@login_required
def faq_update(request, pk):
    company_data = data_company()
    faq = get_object_or_404(Faq, id=pk)

    if request.method == 'POST':
        faq_form = FaqForm(request.POST, request.FILES, instance=faq)
        if faq_form.is_valid():
            faq_form.save()
            return redirect('app_user:faqs')

    else:
        faq_form = FaqForm(instance=faq)

    context = {'company_data': company_data, 'faq': faq, 'faq_form': faq_form}
    return render(request, 'app_user/pages/faq_update.html', context)


############### PRIVACY ###############
@login_required
def privacy_update(request):
    company_data = data_company()
    privacy = Privacy.objects.all().last()

    if request.method == 'POST':
        privacy_form = PrivacyForm(request.POST, request.FILES, instance=privacy)
        if privacy_form.is_valid():
            privacy_form.save()
            return redirect('app_user:admin_index')
    else:
        privacy_form = PrivacyForm(instance=privacy)

    context = {'company_data': company_data, 'privacy': privacy, 'privacy_form': privacy_form}
    return render(request, 'app_user/pages/privacy.html', context)


############### SOCIAL MEDIA ###############
@login_required
def social_media(request):
    company_data = data_company()
    social_media = SocialMedia.objects.all()

    if request.method == 'POST':
        social_media_id = request.POST.get('deleteSocialMediaInput', '')
        SocialMedia.objects.filter(pk=social_media_id).delete()

    context = {'company_data': company_data, 'social_media': social_media}
    return render(request, 'app_user/pages/social_media.html', context)


@login_required
def social_media_create(request):
    company_data = data_company()
    if request.method == 'POST':
        social_media_form = SocialMediaForm(request.POST, request.FILES)
        if social_media_form.is_valid():

            social_name = social_media_form.cleaned_data.get('name')
            print(f"Esta es la red social: {social_name}")
            if social_name == '01':
                social_media_form.instance.icon_class = "fab fa-facebook"
                social_media_form.instance.icon_class_footer = "fa fa-facebook"
            elif social_name == '02':
                social_media_form.instance.icon_class = "fab fa-twitter"
                social_media_form.instance.icon_class_footer = "fa fa-twitter"
            elif social_name == '03':
                social_media_form.instance.icon_class = "fab fa-instagram"
                social_media_form.instance.icon_class_footer = "fa fa-instagram"
            elif social_name == '04':
                social_media_form.instance.icon_class = "fab fa-tiktok"
                social_media_form.instance.icon_class_footer = "fa fa-camera-retro"
            elif social_name == '05':
                social_media_form.instance.icon_class = "fab fa-youtube"
                social_media_form.instance.icon_class_footer = "fa fa-youtube"
            elif social_name == '06':
                social_media_form.instance.icon_class = "fab fa-linkedin"
                social_media_form.instance.icon_class_footer = "fa fa-linkedin"
            elif social_name == '07':
                social_media_form.instance.icon_class = "fab fa-whatsapp"
                social_media_form.instance.icon_class_footer = "fa fa-linkedin"

            new_social_media = social_media_form.save()
            return redirect('app_user:social_media')
    else:
        social_media_form = SocialMediaForm()

    return render(request, 'app_user/pages/social_media_create.html',
                  {'company_data': company_data, 'social_media_form': social_media_form})


@login_required
def social_media_update(request, pk):
    company_data = data_company()
    social_media = get_object_or_404(SocialMedia, id=pk)

    if request.method == 'POST':
        social_media_form = SocialMediaForm(request.POST, request.FILES, instance=social_media)
        if social_media_form.is_valid():

            social_name = social_media_form.cleaned_data.get('name')
            print(f"Esta es la red social: {social_name}")
            if social_name == '01':
                social_media_form.instance.icon_class = "fab fa-facebook"
                social_media_form.instance.icon_class_footer = "fa fa-facebook"
            elif social_name == '02':
                social_media_form.instance.icon_class = "fab fa-twitter"
                social_media_form.instance.icon_class_footer = "fa fa-twitter"
            elif social_name == '03':
                social_media_form.instance.icon_class = "fab fa-instagram"
                social_media_form.instance.icon_class_footer = "fa fa-instagram"
            elif social_name == '04':
                social_media_form.instance.icon_class = "fab fa-tiktok"
                social_media_form.instance.icon_class_footer = "fa fa-camera-retro"
            elif social_name == '05':
                social_media_form.instance.icon_class = "fab fa-youtube"
                social_media_form.instance.icon_class_footer = "fa fa-youtube"
            elif social_name == '06':
                social_media_form.instance.icon_class = "fab fa-linkedin"
                social_media_form.instance.icon_class_footer = "fa fa-linkedin"
            elif social_name == '07':
                social_media_form.instance.icon_class = "fab fa-whatsapp"
                social_media_form.instance.icon_class_footer = "fa fa-linkedin"

            social_media_form.save()
            return redirect('app_user:social_media')

    else:
        social_media_form = SocialMediaForm(instance=social_media)

    context = {'company_data': company_data, 'social_media': social_media, 'social_media_form': social_media_form}
    return render(request, 'app_user/pages/social_media_update.html', context)


################# GALERIA (IMAGES - VIDEOS) ##################
@login_required
def galeria_index(request):
    company_data = data_company()
    context = {
        'company_data': company_data
    }
    return render(request, 'app_user/pages/galeria_index.html', context)


############### WORKS ###############
@login_required
def works(request):
    company_data = data_company()
    works = WorkImage.objects.all()

    if request.method == 'POST':
        work_id = request.POST.get('deleteWorkInput', '')
        WorkImage.objects.filter(pk=work_id).delete()

    context = {'company_data': company_data, 'works': works}
    return render(request, 'app_user/pages/works.html', context)


@login_required
def work_create(request):
    company_data = data_company()
    if request.method == 'POST':
        work_form = WorkForm(request.POST, request.FILES)
        if work_form.is_valid():
            images = request.FILES.getlist('image')
            for idx, image in enumerate(images, start=1):
                # Abre la imagen utilizando Pillow
                img = Image.open(image)
                # Redimensiona la imagen si su ancho es mayor que 1280 píxeles
                max_width = 1280
                if img.width > max_width:
                    # Calcula la altura manteniendo la relación de aspecto
                    height = int((max_width / img.width) * img.height)
                    img = img.resize((max_width, height), Image.LANCZOS)
                # Convierte la imagen a formato WEBP
                buffer = BytesIO()
                img.save(buffer, 'WEBP')
                buffer.seek(0)
                # Crea un objeto File a partir de la imagen convertida
                image_file = File(buffer)
                # Asigna un nombre personalizado a la imagen
                custom_name = f'{idx}.webp'
                # Asigna el nombre personalizado al archivo
                image_file.name = custom_name
                # Crea un objeto WorkImage con la imagen y el nombre personalizado
                work_image = WorkImage(image=image_file)
                # Guarda la instancia del modelo en la base de datos
                work_image.save()

            messages.success(request, 'Imágenes cargadas exitosamente.')
            return redirect('app_user:works')
    else:
        work_form = WorkForm()

    return render(request, 'app_user/pages/work_create.html', {'company_data': company_data, 'work_form': work_form})


############### VIDEOS ###############
@login_required
def videos(request):
    company_data = data_company()
    videos = WorkVideo.objects.all()

    if request.method == 'POST':
        video_id = request.POST.get('deleteVideoInput', '')
        WorkVideo.objects.filter(pk=video_id).delete()

    context = {'videos': videos, 'company_data': company_data}
    return render(request, 'app_user/pages/videos.html', context)


@login_required
def video_create(request):
    company_data = data_company()
    if request.method == 'POST':
        video_form = WorkVideoForm(request.POST, request.FILES)
        if video_form.is_valid():
            new_video = video_form.save()
            return redirect('app_user:videos')
    else:
        video_form = WorkVideoForm()

    return render(request, 'app_user/pages/video_create.html', {'video_form': video_form, 'company_data': company_data})


@login_required
def video_update(request, pk):
    company_data = data_company()
    video = get_object_or_404(WorkVideo, id=pk)

    if request.method == 'POST':
        video_form = WorkVideoForm(request.POST, request.FILES, instance=video)
        if video_form.is_valid():
            video_form.save()
            return redirect('app_user:videos')

    else:
        video_form = WorkVideoForm(instance=video)

    context = {'video': video, 'video_form': video_form, 'company_data': company_data}
    return render(request, 'app_user/pages/video_update.html', context)


############### TEAM ###############
@login_required
def team(request):
    company_data = data_company()
    team = TeamPerson.objects.all()

    if request.method == 'POST':
        team_person_id = request.POST.get('deleteteamPersonInput', '')
        TeamPerson.objects.filter(pk=team_person_id).delete()

    context = {'team': team, 'company_data': company_data}
    return render(request, 'app_user/pages/team.html', context)


@login_required
def team_person_create(request):
    company_data = data_company()
    if request.method == 'POST':
        team_person_form = TeamPersonForm(request.POST, request.FILES)
        if team_person_form.is_valid():
            new_partner = team_person_form.save()
            return redirect('app_user:team')
    else:
        team_person_form = TeamPersonForm()

    return render(request, 'app_user/pages/team_person_create.html',
                  {'team_person_form': team_person_form, 'company_data': company_data})


@login_required
def team_person_update(request, pk):
    company_data = data_company()
    team_person = get_object_or_404(TeamPerson, id=pk)

    if request.method == 'POST':
        team_person_form = TeamPersonForm(request.POST, request.FILES, instance=team_person)
        if team_person_form.is_valid():
            team_person_form.save()
            return redirect('app_user:team')

    else:
        team_person_form = TeamPersonForm(instance=team_person)

    context = {'team_person': team_person, 'team_person_form': team_person_form, 'company_data': company_data}
    return render(request, 'app_user/pages/team_person_update.html', context)

#############schedule############
@login_required
def schedule(request):
    company_data = data_company()
    schedule = Schedule.objects.all().order_by('days')

    if request.method == 'POST':
        schedule_id = request.POST.get('deleteScheduleInput', '')
        Schedule.objects.filter(pk=schedule_id).delete()

    context = {'company_data': company_data, 'schedules': schedule}
    
    return render(request, 'app_user/pages/schedule.html', context)


@login_required
def schedule_create(request):
    company_data = data_company()
    if request.method == 'POST':
        schedule_form = ScheduleForm(request.POST, request.FILES)
        if schedule_form.is_valid():
            schedule_form.save()
        return redirect('app_user:schedule')
    else:
        schedule_form = ScheduleForm()

    return render(request, 'app_user/pages/schedule_create.html',
                  {'company_data': company_data, 'schedule_form': schedule_form})


@login_required
def schedule_update(request, pk):
    company_data = data_company()
    schedule = get_object_or_404(Schedule, id=pk)

    if request.method == 'POST':
        schedule_form = ScheduleForm(request.POST, request.FILES, instance=schedule)
        if schedule_form.is_valid():
            schedule_form.save()
            return redirect('app_user:schedule')

    else:
        schedule_form = ScheduleForm(instance=schedule)

    context = {'company_data': company_data, 'schedule': schedule, 'schedule_form': schedule_form}
    return render(request, 'app_user/pages/schedule_update.html', context)
