from django.db import models

# Create your models here.
class MyModel(models.Model):
    # This is for primary key which will incrise automatically 
    auto_field = models.AutoField(primary_key=True)

    # BigAutoField: Similar to AutoField, but suitable for larger integer ranges. It’s a 64-bit integer, guaranteed to fit integers between 1 and 9223372036854775807.
    # big_auto_field = models.BigAutoField(primary_key=True)


    # To store images, filse im databse we can use binary field
    binary_field = models.BigAutoField()

    # A field type that represents a boolean value, allowing for storage and retrieval of True or False values.
    boolean_field = models.BooleanField()

    # CharField: Stores a string of a fixed length. Commonly used for short to medium-length strings.
    char_field = models.CharField(max_length=255)


    # DateField: Stores a date value (year, month, and day) without any time information.
    date_field = models.DateField()

    # DateTimeField: This stores both date and time information.
    date_time_field = models.DateTimeField()

    # DecimalField: Stores decimal numbers with a fixed number of digits before and after the decimal point.
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)

    # DurationField: A field type used to store a duration of time, such as the length of a video or the duration of an event, in a compact and standardized format.
    duration_field = models.DurationField()

    # EmailField: A field type used to store and validate email addresses.
    email_field = models.EmailField()

    # FileField: Represents a file upload. The file is saved to the file system, and the path is stored in the database.
    file_field = models.FileField(upload_to='files/')

    # GenericIPAddressField: Stores an IP address, either IPv4 or IPv6.
    generic_ip_address = models.GenericIPAddressField()

    # ImageField: Similar toFileField, but optimized for image uploads It provides additional validation and thumbnail generation.
    image_field = models.ImageField(upload_to='images/')

    # JSONField: Stores JSON-encoded data, allowing flexible and schema-less storage of structured data.
    json_field = models.JSONField()

    # NullBooleanField: Similar toBooleanField, but allows for an additional NULL option.
    null_boolean_field = models.NullBooleanField()

    # URLField: A field type used to store and validate URLs (Uniform Resource Locators) as strings.
    url_field = models.URLField()

    