from django import forms
from django.forms import ClearableFileInput
from app_core.models import Contact, Banner, About, Skill, Counter, Service, SubService, Testimonial, Partner, Faq, \
    Privacy, WorkImage, SocialMedia, WorkVideo, TeamPerson, Schedule
from django.utils.text import slugify

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


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['location', 'address', 'city', 'state', 'postal_code', 'phone1', 'phone2', 'email', 'image_contact', 'latitude',
                  'longitude']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'phone1': forms.TextInput(attrs={'class': 'form-control'}),
            'phone2': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
        }


class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['image','image_sections', 'title', 'title2', 'subtitle', 'description', 'insurance']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title2': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
            'insurance': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['company_name', 'image','image_1','image_2', 'image_mission_vision', 'about', 'mision', 'vision','counter','counter_value', 'image_google', 'url_google']
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'counter': forms.TextInput(attrs={'class': 'form-control'}),
            'counter_value': forms.TextInput(attrs={'class': 'form-control'}),
            'url_google': forms.TextInput(attrs={'class': 'form-control', 'type': 'url'}),
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['title1', 'description1', 'title2', 'description2', 'title3', 'description3', 'title4', 'description4']
        widgets = {
            'title1': forms.TextInput(attrs={'class': 'form-control'}),
            'description1': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
            'title2': forms.TextInput(attrs={'class': 'form-control'}),
            'description2': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
            'title3': forms.TextInput(attrs={'class': 'form-control'}),
            'description3': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
            'title4': forms.TextInput(attrs={'class': 'form-control'}),
            'description4': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
        }



class CounterForm(forms.ModelForm):
    icon1 = forms.ChoiceField(
        choices=FLATICON_ICONS_CHOICES,
        label='Icon 1',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    icon2 = forms.ChoiceField(
        choices=FLATICON_ICONS_CHOICES,
        label='Icon 2',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    icon3 = forms.ChoiceField(
        choices=FLATICON_ICONS_CHOICES,
        label='Icon 3',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    icon4 = forms.ChoiceField(
        choices=FLATICON_ICONS_CHOICES,
        label='Icon 4',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Counter
        fields = [
            'title1',
            'number1',
            'symbol1',
            'icon1',
            'title2',
            'number2',
            'symbol2',
            'icon2',
            'title3',
            'number3',
            'symbol3',
            'icon3',
            'title4',
            'number4',
            'symbol4',
            'icon4'
        ]
        widgets = {
            'title1': forms.TextInput(attrs={'class': 'form-control'}),
            'number1': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'symbol1': forms.TextInput(attrs={'class': 'form-control'}),
            'icon1': forms.Select(attrs={'class': 'form-control'}),
            'title2': forms.TextInput(attrs={'class': 'form-control'}),
            'number2': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'symbol2': forms.TextInput(attrs={'class': 'form-control'}),
            'icon2': forms.Select(attrs={'class': 'form-control'}),
            'title3': forms.TextInput(attrs={'class': 'form-control'}),
            'number3': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'symbol3': forms.TextInput(attrs={'class': 'form-control'}),
            'icon3': forms.Select(attrs={'class': 'form-control'}),
            'title4': forms.TextInput(attrs={'class': 'form-control'}),
            'number4': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number'}),
            'symbol4': forms.TextInput(attrs={'class': 'form-control'}),
            'icon4': forms.Select(attrs={'class': 'form-control'}),
        }


class ServiceForm(forms.ModelForm):
    icon = forms.ChoiceField(
        choices=FLATICON_ICONS_CHOICES,
        label='Icon',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    icon_mobile = forms.ChoiceField(
        choices=ICONS_SERVICES_MOBILE,
        label='Icon',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Service
        fields = ['image', 'image_large', 'image_small', 'icon', 'icon_mobile', 'name', 'title','slug', 'description', 'description_finish']
        widgets = {
            'icon': forms.Select(attrs={'class': 'form-control'}),
            'icon_mobile': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ServiceDeleteForm(forms.Form):
    id_to_delete = forms.IntegerField(widget=forms.HiddenInput())


class SubServiceForm(forms.ModelForm):
    class Meta:
        model = SubService
        fields = ['service', 'image', 'title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TestimonialForm(forms.ModelForm):
    stars = forms.ChoiceField(
        choices=STARS_REVIEW_CHOICES,
        label='Stars',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Testimonial
        fields = ['image', 'name', 'location', 'stars', 'url', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'id': 'position'}),
            'stars': forms.Select(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'type': 'url'}),
            'description': forms.Textarea(attrs={'class': 'resizable_textarea form-control'}),
        }


class TestimonialDeleteForm(forms.Form):
    id_to_delete = forms.IntegerField(widget=forms.HiddenInput())


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['image', 'url']
        widgets = {
            'url': forms.TextInput(attrs={'class': 'form-control', 'type': 'url'}),
        }


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PrivacyForm(forms.ModelForm):
    class Meta:
        model = Privacy
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }


class WorkForm(forms.ModelForm):
    class Meta:
        model = WorkImage
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(attrs={'allow_multiple_selected': True})
        }


class SocialMediaForm(forms.ModelForm):
    name = forms.ChoiceField(
        choices=SOCIAL_MEDIA_CHOICES,
        label='Name',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = SocialMedia
        fields = ['name', 'url']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'type': 'url'}),
        }


class WorkVideoForm(forms.ModelForm):
    image = forms.ImageField(
        label='Image',
        required=True,
    )

    class Meta:
        model = WorkVideo
        fields = ['title', 'image', 'url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'type': 'url', 'required': True}),
        }


class TeamPersonForm(forms.ModelForm):
    class Meta:
        model = TeamPerson
        fields = ['image', 'name', 'position', 'phone', 'facebook_url', 'instagram_url', 'tiktok_url', 'x_url']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control', 'type': 'url'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control', 'type': 'url'}),
            'tiktok_url': forms.TextInput(attrs={'class': 'form-control', 'type': 'url'}),
            'x_url': forms.TextInput(attrs={'class': 'form-control', 'type': 'url'}),
        }

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['days', 'full_time','activate','short_mode', 'open_time', 'close_time']
        widgets = {
            'days': forms.Select(attrs={'class': 'form-control'}),
            'open_time': forms.TextInput(attrs={'class': 'form-control'}),
            'close_time': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        full_time = cleaned_data.get("full_time")
        open_time = cleaned_data.get("open_time")
        close_time = cleaned_data.get("close_time")

        # Validar que si no es full_time, open_time y close_time sean requeridos
        if not full_time and (not open_time or not close_time):
            raise forms.ValidationError("Open time and close time are required if full-time is not selected.")

        return cleaned_data