from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Service, Contact

@receiver(pre_save, sender=Service)
def update_service_slug(sender, instance, **kwargs):
    """
    Actualiza el slug del servicio antes de guardar.
    Se basa en el último contacto y el nombre del servicio.
    """
    contact = Contact.objects.last()  # Obtener el último contacto
    if not instance.slug or instance.name != sender.objects.filter(pk=instance.pk).values_list('name', flat=True).first():
        instance.slug = generate_service_slug(instance, contact)


@receiver(post_save, sender=Contact)
def update_services_on_contact_change(sender, instance, **kwargs):
    """
    Actualiza los slugs de todos los servicios cuando se guarda un contacto.
    """
    contact = instance  # Instancia actual de Contact
    services = Service.objects.all()

    for service in services:
        updated_slug = generate_service_slug(service, contact)
        if service.slug != updated_slug:  # Evitar saves innecesarios
            service.slug = updated_slug
            service.save()


def generate_service_slug(service, contact):
    """
    Genera el slug para un servicio basado en su nombre y el contacto.
    Si no hay contacto o ciudad, usa valores predeterminados.
    """
    base_slug = f"{service.name or service.id}-service"
    if contact and contact.city:
        return slugify(f"{base_slug}-{contact.city}")
    return slugify(base_slug)