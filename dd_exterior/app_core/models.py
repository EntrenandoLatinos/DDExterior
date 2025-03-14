import os
from django.db import models
from io import BytesIO
from django.core.files.base import ContentFile
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from ckeditor.fields import RichTextField

# Opciones para el campo de selección
CATEGORY_CHOICES = [
    ('01', 'Roofing'),
    ('02', 'Flat Roofing'),
    ('04', 'Siding'),
    ('05', 'Gutter'),
    ('06', 'Window'),
    ('07', 'Carpentry'),
    ('08', 'Remodeling'),
]

SOCIAL_MEDIA_CHOICES = [
    ('01', 'Facebook'),
    ('02', 'Twitter'),
    ('03', 'Instagram'),
    ('04', 'TikTok'),
    ('05', 'YouTube'),
    ('06', 'LinkedIn'),
    ('07', 'Whatsapp'),
]

STARS_REVIEW_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]

FLATICON_ICONS_CHOICES = [
    ('01', 'flaticon-factory'),
    ('02', 'flaticon-factory-1'),
    ('03', 'flaticon-engineer'),
    ('04', 'flaticon-valve'),
    ('05', 'flaticon-conveyor'),
    ('06', 'flaticon-oil'),
    ('07', 'flaticon-truck'),
    ('08', 'flaticon-forklift'),
    ('09', 'flaticon-voltmeter'),
    ('10', 'flaticon-fuel-truck'),
    ('11', 'flaticon-gear'),
    ('12', 'flaticon-fuel-station'),
    ('13', 'flaticon-robotic-arm'),
    ('14', 'flaticon-product'),
    ('15', 'flaticon-worker'),
    ('16', 'flaticon-robot-arm'),
    ('17', 'flaticon-help'),
    ('18', 'flaticon-conveyor-1'),
    ('19', 'flaticon-factory-2'),
    ('20', 'flaticon-optimization'),
    ('21', 'flaticon-wrench'),
    ('22', 'flaticon-crane'),
    ('23', 'flaticon-engineer-1'),
    ('24', 'flaticon-design-tools'),
    ('25', 'flaticon-construction'),
    ('26', 'flaticon-settings'),
    ('27', 'flaticon-idea'),
    ('28', 'flaticon-calculator'),
    ('29', 'flaticon-cpu'),
    ('30', 'flaticon-repair-tools'),
    ('31', 'flaticon-internet'),
    ('32', 'flaticon-analytics'),
    ('33', 'flaticon-printer'),
    ('34', 'flaticon-helmet'),
    ('35', 'flaticon-presentation'),
    ('36', 'flaticon-alarm-clock'),
    ('37', 'flaticon-bar-chart'),
    ('38', 'flaticon-microphone'),
    ('39', 'flaticon-shield'),
    ('40', 'flaticon-loupe'),
    ('41', 'flaticon-settings-1'),
    ('42', 'flaticon-monitor'),
    ('43', 'flaticon-shopping-cart'),
    ('44', 'flaticon-home'),
    ('45', 'flaticon-message'),
    ('46', 'flaticon-heart'),
    ('47', 'flaticon-user'),
    ('48', 'flaticon-play-button'),
    ('49', 'flaticon-planet-earth'),
    ('50', 'flaticon-settings-2'),
]

ICONS_SERVICES_MOBILE = [
    ('01', 'Roofing'),
    ('02', 'Siding'),
    ('03', 'Gutter'),
    ('04', 'Window'),
    ('05', 'Paint'),
    ('06', 'Deck'),
    ('07', 'Framing'),
    ('08', 'Drywall'),
    ('09', 'Demolition'),
    ('10', 'Other'),
]

SCHEDULE_CHOICES = [
    ('01', 'Monday-Friday'),
    ('02', 'Saturday'),
    ('03', 'Saturday & Sunday'),
    ('04', 'Monday-Sunday'),
]

STATES_CHOICES = [
    ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'),
    ('CA', 'California'), ('NC', 'Carolina del Norte'), ('SC', 'Carolina del Sur'), ('CO', 'Colorado'),
    ('CT', 'Connecticut'), ('ND', 'Dakota del Norte'), ('SD', 'Dakota del Sur'), ('DE', 'Delaware'),
    ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawái'), ('ID', 'Idaho'),
    ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'),
    ('KY', 'Kentucky'), ('LA', 'Luisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
    ('MA', 'Massachusetts'), ('MI', 'Míchigan'), ('MN', 'Minnesota'), ('MS', 'Misisipi'),
    ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'),
    ('NJ', 'Nueva Jersey'), ('NY', 'Nueva York'), ('NH', 'Nueva Hampshire'), ('NM', 'Nuevo México'),
    ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregón'), ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'),
    ('VT', 'Vermont'), ('VA', 'Virginia'), ('WV', 'Virginia Occidental'), ('WA', 'Washington'),
    ('WI', 'Wisconsin'), ('WY', 'Wyoming')
]


# Create your models here.
class AuditoriaFecha(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Contact(AuditoriaFecha):
    location = models.CharField("Location", max_length=300, null=True, blank=True)
    address = models.CharField("Address", max_length=300, null=True, blank=True)
    city = models.CharField("City", max_length=100, null=True, blank=True)
    state = models.CharField("State", max_length=2, choices=STATES_CHOICES, null=True, blank=True)
    postal_code = models.CharField("Postal Code", max_length=100, null=True, blank=True)
    phone1 = models.CharField("Phone 2", max_length=60, null=True, blank=True)
    phone2 = models.CharField("Phone 1", max_length=60, null=True, blank=True)
    email = models.EmailField("Email", null=True, blank=True)
    image_contact = models.ImageField(upload_to='contact/', null=True, blank=True)
    latitude = models.FloatField("latitude", null=True, blank=True)
    longitude = models.FloatField("longitude", null=True, blank=True)

    def __str__(self):
        return "{0}".format(str(self.email))

    class Meta:
        ordering = ['id']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class Banner(AuditoriaFecha):
    image = models.ImageField(upload_to='banner/', null=True, blank=True)
    image_sections = models.ImageField(upload_to='banner/', null=True, blank=True)
    title = models.CharField("Banner title", max_length=300, null=True, blank=True, default="")
    title2 = models.CharField("Banner title2", max_length=300, null=True, blank=True, default="")
    subtitle = models.CharField("Banner subtitle", max_length=300, null=True, blank=True, default="")
    description = models.TextField("Description", max_length=300, null=True, blank=True)
    insurance = models.CharField("Insurance", max_length=300, null=True, blank=True, default="")

    def __str__(self):
        return "{0}".format(str(self.title))

    class Meta:
        ordering = ['id']
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'


class About(AuditoriaFecha):
    company_name = models.CharField("Company Name", max_length=300, null=True, blank=True, default="")
    image = models.ImageField(upload_to='about/', null=True, blank=True)
    image_1 = models.ImageField(upload_to='about/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='about/', null=True, blank=True)
    image_mission_vision = models.ImageField(upload_to='about/', null=True, blank=True)
    about = RichTextField("About", null=True, blank=True)
    mision = RichTextField("Mission", null=True, blank=True)
    vision = RichTextField("Vision", null=True, blank=True)
    counter = models.CharField("Counter", max_length=200, null=True, blank=True)
    counter_value = models.IntegerField("Counter Value", null=True, blank=True)
    image_google = models.ImageField(upload_to='about/', null=True, blank=True)
    url_google = models.URLField("URL Google Business", null=True, blank=True)
    is_gallery = models.BooleanField(default=False)
    is_team = models.BooleanField(default=False)

    def __str__(self):
        return "{0}".format(str(self.id))

    class Meta:
        ordering = ['id']
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'


class Skill(AuditoriaFecha):
    image1 = models.ImageField(upload_to='skill/', null=True, blank=True)
    title1 = models.CharField("Skill title 1", max_length=300, null=True, blank=True)
    description1 = models.TextField("Description 1", null=True, blank=True)
    image2 = models.ImageField(upload_to='skill/', null=True, blank=True)
    title2 = models.CharField("Skill title 2", max_length=300, null=True, blank=True)
    description2 = models.TextField("Description 2", null=True, blank=True)
    image3 = models.ImageField(upload_to='skill/', null=True, blank=True)
    title3 = models.CharField("Skill title 3", max_length=300, null=True, blank=True)
    description3 = models.TextField("Description 3", null=True, blank=True)
    image4 = models.ImageField(upload_to='skill/', null=True, blank=True)
    title4 = models.CharField("Skill title 3", max_length=300, null=True, blank=True)
    description4 = models.TextField("Description 3", null=True, blank=True)

    def __str__(self):
        return "{0}".format(str(self.title1))

    class Meta:
        ordering = ['id']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class Counter(AuditoriaFecha):
    title1 = models.CharField("Title 1", max_length=300, null=True, blank=True)
    number1 = models.IntegerField("Number 1", null=True, blank=True)
    symbol1 = models.CharField("Symbol 1", max_length=300, null=True, blank=True)
    icon1 = models.CharField("Icon 1", max_length=2, choices=FLATICON_ICONS_CHOICES, null=True, blank=True)
    title2 = models.CharField("Title 2", max_length=300, null=True, blank=True)
    number2 = models.IntegerField("Number 2", null=True, blank=True)
    symbol2 = models.CharField("Symbol 2", max_length=300, null=True, blank=True)
    icon2 = models.CharField("Icon 2", max_length=2, choices=FLATICON_ICONS_CHOICES, null=True, blank=True)
    title3 = models.CharField("Title 3", max_length=300, null=True, blank=True)
    number3 = models.IntegerField("Number 3", null=True, blank=True)
    symbol3 = models.CharField("Symbol 3", max_length=300, null=True, blank=True)
    icon3 = models.CharField("Icon 3", max_length=2, choices=FLATICON_ICONS_CHOICES, null=True, blank=True)
    title4 = models.CharField("Title 4", max_length=300, null=True, blank=True)
    number4 = models.IntegerField("Number 4", null=True, blank=True)
    symbol4 = models.CharField("Symbol 4", max_length=300, null=True, blank=True)
    icon4 = models.CharField("Icon 4", max_length=2, choices=FLATICON_ICONS_CHOICES, null=True, blank=True)

    def __str__(self):
        return "{0}".format(str(self.title1))

    class Meta:
        ordering = ['id']
        verbose_name = 'Counter'
        verbose_name_plural = 'Counters'


class Service(AuditoriaFecha):
    image = models.ImageField(upload_to='service/', null=True, blank=True)
    image_large = models.ImageField(upload_to='service/', null=True, blank=True)
    image_small = models.ImageField(upload_to='service/', null=True, blank=True)
    icon = models.CharField("Icon", max_length=2, choices=FLATICON_ICONS_CHOICES, null=True, blank=True)
    icon_mobile = models.CharField("Icon Mobile", max_length=2, choices=ICONS_SERVICES_MOBILE, null=True, blank=True)
    name=models.CharField("Name", max_length=300, null=True, blank=True)
    title = models.CharField("Service title", max_length=300, null=True, blank=True)
    slug = models.SlugField(max_length=150, unique=True, null=True, blank=True)
    description = RichTextField("Description", null=True, blank=True)
    description_finish = RichTextField("Finish Description", null=True, blank=True)

    def __str__(self):
        return "{0}".format(str(self.title))

    class Meta:
        ordering = ['id']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class SubService(AuditoriaFecha):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_subservice')
    image = models.ImageField(upload_to='subservice/', null=True, blank=True)
    title = models.CharField("Subservice Name", max_length=300, null=True, blank=True)
    description = RichTextField("Description", null=True, blank=True)

    def __str__(self):
        return "{0}".format(str(self.title))

    class Meta:
        ordering = ['id']
        verbose_name = 'SubService'
        verbose_name_plural = 'SubServices'


class WorkImage(AuditoriaFecha):
    category = models.CharField("Category", null=True, blank=True, max_length=2, choices=CATEGORY_CHOICES)
    title = models.CharField("Image title", max_length=300, null=True, blank=True)
    description = models.TextField("Description", null=True, blank=True)
    image = models.ImageField(upload_to='work_image/')

    def __str__(self):
        return "{0}".format(str(self.title))

    def save(self, *args, **kwargs):
        # Si el objeto ya existe (no está siendo añadido por primera vez), guarda y retorna
        if not self._state.adding and self.pk is not None:
            super().save(*args, **kwargs)
            return

        # Procesa la imagen solo cuando se está añadiendo por primera vez
        if self.image:
            img = Image.open(self.image)

            # Define la calidad inicial
            quality = 90

            # Crear un BytesIO para almacenar la imagen temporal
            img_io = BytesIO()

            # Reduce la calidad de la imagen hasta que sea menor o igual a 100KB
            while True:
                # Guarda la imagen en formato WEBP con la calidad especificada
                img_io.truncate(0)
                img_io.seek(0)
                img.save(img_io, 'WEBP', quality=quality)

                # Obtener el tamaño del archivo resultante en bytes
                size = img_io.tell()

                # Si el tamaño del archivo es menor o igual a 100KB, se detiene el bucle
                if size <= 100 * 1024:
                    break

                # Reduce la calidad para la próxima iteración
                quality -= 5

                # Si la calidad llega a 0, se detiene el bucle para evitar calidad muy baja
                if quality <= 0:
                    break

            # Guardar la imagen redimensionada y optimizada en el campo image
            img_content = ContentFile(img_io.getvalue(), self.image.name)
            self.image.save(self.image.name, img_content, save=False)

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['id']
        verbose_name = 'Work image'
        verbose_name_plural = 'Work images'


@receiver(pre_delete, sender=WorkImage)
def delete_gallery_image(sender, instance, **kwargs):
    file_path = instance.image.path
    if os.path.exists(file_path):
        os.remove(file_path)


class WorkVideo(AuditoriaFecha):
    title = models.CharField("Video title", max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to='work_image/')
    url = models.URLField("URL")

    def __str__(self):
        return "{0}".format(str(self.url))

    class Meta:
        ordering = ['id']
        verbose_name = 'Work video'
        verbose_name_plural = 'Work videos'


class Testimonial(AuditoriaFecha):
    image = models.ImageField(upload_to='testimonial/', null=True, blank=True)
    name = models.CharField("Name", max_length=300, null=True, blank=True)
    location = models.CharField("Location", max_length=300, null=True, blank=True)
    stars = models.CharField("Stars", max_length=1, choices=STARS_REVIEW_CHOICES, null=True, blank=True)
    url = models.URLField("URL", null=True, blank=True)
    description = models.TextField("Description", null=True, blank=True)

    def __str__(self):
        return "{0}".format(str(self.name))

    class Meta:
        ordering = ['id']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'


class Partner(AuditoriaFecha):
    image = models.ImageField(upload_to='partner/', null=True, blank=True)
    url = models.URLField("URL", null=True, blank=True)

    def __str__(self):
        return "{0}".format(str(self.id))

    class Meta:
        ordering = ['id']
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'


class Faq(AuditoriaFecha):
    title = models.CharField("Title", max_length=300, null=True, blank=True)
    description = RichTextField("Description", null=True, blank=True)

    def __str__(self):
        return "{0}".format(str(self.title))

    class Meta:
        ordering = ['id']
        verbose_name = 'Faq'
        verbose_name_plural = 'Faqs'


class Privacy(AuditoriaFecha):
    title = models.CharField("Title", max_length=300, null=True, blank=True)
    description = RichTextField("Description", null=True, blank=True)

    def __str__(self):
        return "{0}".format(str(self.title))

    class Meta:
        ordering = ['id']
        verbose_name = 'Privacy'
        verbose_name_plural = 'Privacies'


class SocialMedia(AuditoriaFecha):
    name = models.CharField("Name", max_length=2, choices=SOCIAL_MEDIA_CHOICES)
    url = models.URLField("URL")
    icon_class = models.CharField("Icon class", max_length=150)
    icon_class_footer = models.CharField("Icon class footer", max_length=150)

    def __str__(self):
        return "{0}".format(str(self.get_name_display()))

    class Meta:
        ordering = ['id']
        verbose_name = 'SocialMedia'
        verbose_name_plural = 'SocialMedias'


class TeamPerson(AuditoriaFecha):
    image = models.ImageField(upload_to='team_image/', null=True, blank=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    position = models.CharField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=60, null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    tiktok_url = models.URLField(null=True, blank=True)
    x_url = models.URLField(null=True, blank=True)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return "{0}".format(str(self.name))

    class Meta:
        ordering = ['id']
        verbose_name = 'Team Person'
        verbose_name_plural = 'Team'

class Schedule(AuditoriaFecha):
    days = models.CharField("Days", max_length=2, choices=SCHEDULE_CHOICES, null=True, blank=True)
    full_time = models.BooleanField(default=False)
    activate = models.BooleanField(default=False)
    short_mode = models.BooleanField(default=False)
    open_time = models.CharField("Open time", max_length=30, null=True, blank=True)
    close_time = models.CharField("Close time", max_length=30, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Verificar si ya existe una instancia con el mismo valor de days
        existing_schedule = Schedule.objects.filter(days=self.days).exclude(id=self.id).first()

        if existing_schedule:
            existing_schedule.delete()

        super(Schedule, self).save(*args, **kwargs)

    def get_days_display(self):
    # Devuelve la representación legible
        return dict(SCHEDULE_CHOICES).get(self.days, '')

    def get_days_short(self):
        # Devuelve la representación corta
        return {
            '01': 'M-F',
            '02': 'S',
            '03': 'Weekend',
            '04': 'M-S'
        }.get(self.days, self.days)

    def __str__(self):
        return "{0}: {1}".format(self.get_days_display(), "Full Time" if self.full_time else f"{self.open_time} - {self.close_time}")
