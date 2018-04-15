# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CountProducts(models.Model):
    category = models.CharField(max_length=50, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'count_products'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class JdHkProductBasemakeup(models.Model):
    first_category = models.CharField(max_length=30, blank=True, null=True)
    third_category = models.CharField(max_length=30, blank=True, null=True)
    second_category = models.CharField(max_length=30, blank=True, null=True)
    img1_address = models.CharField(max_length=255, blank=True, null=True)
    img2_address = models.CharField(max_length=255, blank=True, null=True)
    img3_address = models.CharField(max_length=255, blank=True, null=True)
    img4_address = models.CharField(max_length=255, blank=True, null=True)
    img5_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=255, blank=True, null=True)
    kg = models.CharField(max_length=255, blank=True, null=True)
    good_for_who = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    makeup_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    who_handly = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)
    good_for_skin = models.CharField(max_length=255, blank=True, null=True)
    spf = models.CharField(db_column='SPF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pa = models.CharField(db_column='PA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    platform = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jd_hk_product_baseMakeup'


class JdHkProductCologne(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    store = models.CharField(max_length=50, blank=True, null=True)
    whole_kg = models.CharField(max_length=20, blank=True, null=True)
    produce_address = models.CharField(max_length=20, blank=True, null=True)
    packing = models.CharField(max_length=20, blank=True, null=True)
    perfume_note = models.CharField(max_length=20, blank=True, null=True)
    kg = models.CharField(max_length=20, blank=True, null=True)
    classify = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    good_for_who = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=10, blank=True, null=True)
    who_handly = models.CharField(max_length=20, blank=True, null=True)
    comment_count = models.CharField(max_length=20, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    first_category = models.CharField(max_length=10, blank=True, null=True)
    second_category = models.CharField(max_length=10, blank=True, null=True)
    third_category = models.CharField(max_length=10, blank=True, null=True)
    img1_address = models.CharField(max_length=100, blank=True, null=True)
    img2_address = models.CharField(max_length=100, blank=True, null=True)
    img3_address = models.CharField(max_length=100, blank=True, null=True)
    img4_address = models.CharField(max_length=100, blank=True, null=True)
    img5_address = models.CharField(max_length=100, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jd_hk_product_cologne'


class JdHkProductEye(models.Model):
    first_category = models.CharField(max_length=30, blank=True, null=True)
    third_category = models.CharField(max_length=30, blank=True, null=True)
    second_category = models.CharField(max_length=30, blank=True, null=True)
    img1_address = models.CharField(max_length=255, blank=True, null=True)
    img2_address = models.CharField(max_length=255, blank=True, null=True)
    img3_address = models.CharField(max_length=255, blank=True, null=True)
    img4_address = models.CharField(max_length=255, blank=True, null=True)
    img5_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=255, blank=True, null=True)
    kg = models.CharField(max_length=255, blank=True, null=True)
    good_for_who = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    makeup_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    who_handly = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jd_hk_product_eye'


class JdHkProductFragrantBodyMilk(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    store = models.CharField(max_length=50, blank=True, null=True)
    whole_kg = models.CharField(max_length=20, blank=True, null=True)
    produce_address = models.CharField(max_length=20, blank=True, null=True)
    packing = models.CharField(max_length=20, blank=True, null=True)
    perfume_note = models.CharField(max_length=20, blank=True, null=True)
    kg = models.CharField(max_length=20, blank=True, null=True)
    classify = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    good_for_who = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=10, blank=True, null=True)
    who_handly = models.CharField(max_length=20, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=10, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    first_category = models.CharField(max_length=20, blank=True, null=True)
    second_category = models.CharField(max_length=20, blank=True, null=True)
    third_category = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    img1_address = models.CharField(max_length=100, blank=True, null=True)
    img2_address = models.CharField(max_length=100, blank=True, null=True)
    img3_address = models.CharField(max_length=100, blank=True, null=True)
    img4_address = models.CharField(max_length=100, blank=True, null=True)
    img5_address = models.CharField(max_length=100, blank=True, null=True)
    comment_count = models.IntegerField(blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jd_hk_product_fragrant_body_milk'


class JdHkProductLipstick(models.Model):
    first_category = models.CharField(max_length=30, blank=True, null=True)
    third_category = models.CharField(max_length=30, blank=True, null=True)
    second_category = models.CharField(max_length=30, blank=True, null=True)
    img1_address = models.CharField(max_length=255, blank=True, null=True)
    img2_address = models.CharField(max_length=255, blank=True, null=True)
    img3_address = models.CharField(max_length=255, blank=True, null=True)
    img4_address = models.CharField(max_length=255, blank=True, null=True)
    img5_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=255, blank=True, null=True)
    kg = models.CharField(max_length=255, blank=True, null=True)
    good_for_who = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    makeup_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    who_handly = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jd_hk_product_lipstick'


class JdHkProductPerfume(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    store = models.CharField(max_length=50, blank=True, null=True)
    whole_kg = models.CharField(max_length=20, blank=True, null=True)
    produce_address = models.CharField(max_length=20, blank=True, null=True)
    package = models.CharField(max_length=20, blank=True, null=True)
    perfume_note = models.CharField(max_length=20, blank=True, null=True)
    kg = models.CharField(max_length=20, blank=True, null=True)
    classify = models.CharField(max_length=20, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    good_for_who = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=10, blank=True, null=True)
    who_handly = models.CharField(max_length=10, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    first_category = models.CharField(max_length=10, blank=True, null=True)
    second_category = models.CharField(max_length=10, blank=True, null=True)
    img1_address = models.CharField(max_length=100, blank=True, null=True)
    third_category = models.CharField(max_length=10, blank=True, null=True)
    img2_address = models.CharField(max_length=100, blank=True, null=True)
    img3_address = models.CharField(max_length=100, blank=True, null=True)
    img4_address = models.CharField(max_length=100, blank=True, null=True)
    img5_address = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.IntegerField(blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jd_hk_product_perfume'


class JdHkProductSolidPerfume(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    store = models.CharField(max_length=50, blank=True, null=True)
    whole_kg = models.CharField(max_length=20, blank=True, null=True)
    produce_address = models.CharField(max_length=20, blank=True, null=True)
    packing = models.CharField(max_length=20, blank=True, null=True)
    perfume_note = models.CharField(max_length=20, blank=True, null=True)
    kg = models.CharField(max_length=20, blank=True, null=True)
    classify = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    good_for_who = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=10, blank=True, null=True)
    who_handly = models.CharField(max_length=20, blank=True, null=True)
    comment_count = models.CharField(max_length=10, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    first_category = models.CharField(max_length=20, blank=True, null=True)
    second_category = models.CharField(max_length=20, blank=True, null=True)
    third_category = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    img1_address = models.CharField(max_length=100, blank=True, null=True)
    img2_address = models.CharField(max_length=100, blank=True, null=True)
    img3_address = models.CharField(max_length=100, blank=True, null=True)
    img4_address = models.CharField(max_length=100, blank=True, null=True)
    img5_address = models.CharField(max_length=100, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jd_hk_product_solid_perfume'


class JdProductBasemakeup(models.Model):
    first_category = models.CharField(max_length=30, blank=True, null=True)
    third_category = models.CharField(max_length=30, blank=True, null=True)
    second_category = models.CharField(max_length=30, blank=True, null=True)
    img1_address = models.CharField(max_length=255, blank=True, null=True)
    img2_address = models.CharField(max_length=255, blank=True, null=True)
    img3_address = models.CharField(max_length=255, blank=True, null=True)
    img4_address = models.CharField(max_length=255, blank=True, null=True)
    img5_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=255, blank=True, null=True)
    kg = models.CharField(max_length=255, blank=True, null=True)
    good_for_who = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    makeup_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    who_handly = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)
    good_for_skin = models.CharField(max_length=255, blank=True, null=True)
    spf = models.CharField(db_column='SPF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pa = models.CharField(db_column='PA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    platform = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jd_product_baseMakeup'


class JdProductCologne(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    brand = models.CharField(max_length=20, blank=True, null=True)
    store = models.CharField(max_length=50, blank=True, null=True)
    whole_kg = models.CharField(max_length=20, blank=True, null=True)
    packing = models.CharField(max_length=20, blank=True, null=True)
    perfume_note = models.CharField(max_length=20, blank=True, null=True)
    kg = models.CharField(max_length=20, blank=True, null=True)
    classify = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    good_for_who = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=10, blank=True, null=True)
    who_handly = models.CharField(max_length=20, blank=True, null=True)
    comment_count = models.CharField(max_length=10, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    first_category = models.CharField(max_length=10, blank=True, null=True)
    second_category = models.CharField(max_length=10, blank=True, null=True)
    third_category = models.CharField(max_length=10, blank=True, null=True)
    img1_address = models.CharField(max_length=100, blank=True, null=True)
    img2_address = models.CharField(max_length=100, blank=True, null=True)
    img3_address = models.CharField(max_length=100, blank=True, null=True)
    img4_address = models.CharField(max_length=100, blank=True, null=True)
    img5_address = models.CharField(max_length=100, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jd_product_cologne'


class JdProductEye(models.Model):
    first_category = models.CharField(max_length=30, blank=True, null=True)
    third_category = models.CharField(max_length=30, blank=True, null=True)
    second_category = models.CharField(max_length=30, blank=True, null=True)
    img1_address = models.CharField(max_length=255, blank=True, null=True)
    img2_address = models.CharField(max_length=255, blank=True, null=True)
    img3_address = models.CharField(max_length=255, blank=True, null=True)
    img4_address = models.CharField(max_length=255, blank=True, null=True)
    img5_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=255, blank=True, null=True)
    kg = models.CharField(max_length=255, blank=True, null=True)
    good_for_who = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    makeup_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    who_handly = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jd_product_eye'


class JdProductFragrantBodyMilk(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    store = models.CharField(max_length=50, blank=True, null=True)
    whole_kg = models.CharField(max_length=20, blank=True, null=True)
    packing = models.CharField(max_length=20, blank=True, null=True)
    perfume_note = models.CharField(max_length=20, blank=True, null=True)
    kg = models.CharField(max_length=20, blank=True, null=True)
    classify = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    good_for_who = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=10, blank=True, null=True)
    who_handly = models.CharField(max_length=20, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=10, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    first_category = models.CharField(max_length=10, blank=True, null=True)
    second_category = models.CharField(max_length=10, blank=True, null=True)
    third_category = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    img1_address = models.CharField(max_length=100, blank=True, null=True)
    img2_address = models.CharField(max_length=100, blank=True, null=True)
    img3_address = models.CharField(max_length=100, blank=True, null=True)
    img4_address = models.CharField(max_length=100, blank=True, null=True)
    img5_address = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=20, blank=True, null=True)
    comment_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jd_product_fragrant_body_milk'


class JdProductLipstick(models.Model):
    first_category = models.CharField(max_length=30, blank=True, null=True)
    third_category = models.CharField(max_length=30, blank=True, null=True)
    second_category = models.CharField(max_length=30, blank=True, null=True)
    img1_address = models.CharField(max_length=255, blank=True, null=True)
    img2_address = models.CharField(max_length=255, blank=True, null=True)
    img3_address = models.CharField(max_length=255, blank=True, null=True)
    img4_address = models.CharField(max_length=255, blank=True, null=True)
    img5_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=255, blank=True, null=True)
    kg = models.CharField(max_length=255, blank=True, null=True)
    good_for_who = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    makeup_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    who_handly = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jd_product_lipstick'


class JdProductPerfume(models.Model):
    url_address = models.CharField(max_length=255, blank=True, null=True)
    my_category = models.CharField(max_length=60, blank=True, null=True)
    source = models.CharField(max_length=60, blank=True, null=True)
    first_category = models.CharField(max_length=30, blank=True, null=True)
    third_category = models.CharField(max_length=30, blank=True, null=True)
    second_category = models.CharField(max_length=30, blank=True, null=True)
    img1_address = models.CharField(max_length=255, blank=True, null=True)
    img2_address = models.CharField(max_length=255, blank=True, null=True)
    img3_address = models.CharField(max_length=255, blank=True, null=True)
    img4_address = models.CharField(max_length=255, blank=True, null=True)
    img5_address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=255, blank=True, null=True)
    kg = models.CharField(max_length=255, blank=True, null=True)
    good_for_who = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    who_handly = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.DateTimeField(blank=True, null=True)
    finish_get_data = models.IntegerField(blank=True, null=True)
    store = models.CharField(max_length=60, blank=True, null=True)
    clean_weight = models.CharField(max_length=60, blank=True, null=True)
    package = models.CharField(max_length=60, blank=True, null=True)
    fragrance = models.CharField(max_length=60, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    fragrance_type = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jd_product_perfume'


class JdProductSolidPerfume(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    store = models.CharField(max_length=50, blank=True, null=True)
    whole_kg = models.CharField(max_length=20, blank=True, null=True)
    brand = models.CharField(max_length=20, blank=True, null=True)
    packing = models.CharField(max_length=20, blank=True, null=True)
    perfume_note = models.CharField(max_length=20, blank=True, null=True)
    kg = models.CharField(max_length=20, blank=True, null=True)
    classify = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    good_for_who = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=10, blank=True, null=True)
    who_handly = models.CharField(max_length=10, blank=True, null=True)
    comment_count = models.CharField(max_length=10, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    first_category = models.CharField(max_length=20, blank=True, null=True)
    second_category = models.CharField(max_length=20, blank=True, null=True)
    third_category = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    img1_address = models.CharField(max_length=100, blank=True, null=True)
    img2_address = models.CharField(max_length=100, blank=True, null=True)
    img3_address = models.CharField(max_length=100, blank=True, null=True)
    img4_address = models.CharField(max_length=100, blank=True, null=True)
    img5_address = models.CharField(max_length=100, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jd_product_solid_perfume'


class JdProducts(models.Model):
    first_category = models.CharField(max_length=30, blank=True, null=True)
    third_category = models.CharField(max_length=30, blank=True, null=True)
    second_category = models.CharField(max_length=30, blank=True, null=True)
    img1_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    img2_address = models.CharField(max_length=255, blank=True, null=True)
    img3_address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    img4_address = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    img5_address = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=255, blank=True, null=True)
    kg = models.CharField(max_length=255, blank=True, null=True)
    good_for_who = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    makeup_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    who_handly = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)
    good_for_skin = models.CharField(max_length=255, blank=True, null=True)
    spf = models.CharField(db_column='SPF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pa = models.CharField(db_column='PA', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jd_products'


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    detail_url = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    brand_name = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255)
    comment_count = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)
    default_good_count = models.CharField(max_length=255, blank=True, null=True)
    poor_comment_count = models.CharField(max_length=255, blank=True, null=True)
    good_comment_count = models.CharField(max_length=255, blank=True, null=True)
    good_comment_rate = models.CharField(max_length=255, blank=True, null=True)
    general_comment_count = models.CharField(max_length=255, blank=True, null=True)
    poor_comment_rate = models.CharField(max_length=255, blank=True, null=True)
    general_comment_rate = models.CharField(max_length=255, blank=True, null=True)
    p_id = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class ProductBasemakeup(models.Model):
    first_category = models.CharField(max_length=30, blank=True, null=True)
    third_category = models.CharField(max_length=30, blank=True, null=True)
    second_category = models.CharField(max_length=30, blank=True, null=True)
    img1_address = models.CharField(max_length=255, blank=True, null=True)
    img2_address = models.CharField(max_length=255, blank=True, null=True)
    img3_address = models.CharField(max_length=255, blank=True, null=True)
    img4_address = models.CharField(max_length=255, blank=True, null=True)
    img5_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=50, blank=True, null=True)
    kg = models.CharField(max_length=255, blank=True, null=True)
    good_for_who = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    makeup_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    who_handly = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)
    good_for_skin = models.CharField(max_length=255, blank=True, null=True)
    pa = models.CharField(db_column='PA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    spf = models.CharField(db_column='SPF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    platform = models.CharField(max_length=255, blank=True, null=True)
    key_words = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_baseMakeup'


class ProductComment(models.Model):
    product_id = models.IntegerField()
    comment_id = models.CharField(primary_key=True, max_length=255)
    comment_uid = models.CharField(max_length=255, blank=True, null=True)
    comment_content = models.TextField(blank=True, null=True)
    creation_time = models.CharField(max_length=255, blank=True, null=True)
    after_comment_content = models.CharField(max_length=255)
    get_time = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_comment'


class ProductEye(models.Model):
    first_category = models.CharField(max_length=30, blank=True, null=True)
    third_category = models.CharField(max_length=30, blank=True, null=True)
    second_category = models.CharField(max_length=30, blank=True, null=True)
    img1_address = models.CharField(max_length=255, blank=True, null=True)
    img2_address = models.CharField(max_length=255, blank=True, null=True)
    img3_address = models.CharField(max_length=255, blank=True, null=True)
    img4_address = models.CharField(max_length=255, blank=True, null=True)
    img5_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=50, blank=True, null=True)
    kg = models.CharField(max_length=255, blank=True, null=True)
    good_for_who = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    makeup_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    who_handly = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    key_words = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_eye'


class ProductLipstick(models.Model):
    first_category = models.CharField(max_length=30, blank=True, null=True)
    third_category = models.CharField(max_length=30, blank=True, null=True)
    second_category = models.CharField(max_length=30, blank=True, null=True)
    img1_address = models.CharField(max_length=255, blank=True, null=True)
    img2_address = models.CharField(max_length=255, blank=True, null=True)
    img3_address = models.CharField(max_length=255, blank=True, null=True)
    img4_address = models.CharField(max_length=255, blank=True, null=True)
    img5_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=255, blank=True, null=True)
    kg = models.CharField(max_length=255, blank=True, null=True)
    good_for_who = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    makeup_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    who_handly = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    v_sku_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_lipstick'


class ProductLipstickCopy(models.Model):
    first_category = models.CharField(max_length=30, blank=True, null=True)
    third_category = models.CharField(max_length=30, blank=True, null=True)
    second_category = models.CharField(max_length=30, blank=True, null=True)
    img1_address = models.CharField(max_length=255, blank=True, null=True)
    img2_address = models.CharField(max_length=255, blank=True, null=True)
    img3_address = models.CharField(max_length=255, blank=True, null=True)
    img4_address = models.CharField(max_length=255, blank=True, null=True)
    img5_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=255, blank=True, null=True)
    kg = models.CharField(max_length=255, blank=True, null=True)
    good_for_who = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    makeup_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    who_handly = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_lipstick_copy'


class ProductOtherPerfume(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    brand = models.CharField(max_length=20, blank=True, null=True)
    store = models.CharField(max_length=50, blank=True, null=True)
    whole_kg = models.CharField(max_length=20, blank=True, null=True)
    packing = models.CharField(max_length=20, blank=True, null=True)
    perfume_note = models.CharField(max_length=20, blank=True, null=True)
    kg = models.CharField(max_length=20, blank=True, null=True)
    classify = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    good_for_who = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=10, blank=True, null=True)
    who_handly = models.CharField(max_length=20, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    first_category = models.CharField(max_length=10, blank=True, null=True)
    second_category = models.CharField(max_length=10, blank=True, null=True)
    third_category = models.CharField(max_length=10, blank=True, null=True)
    img1_address = models.CharField(max_length=100, blank=True, null=True)
    img2_address = models.CharField(max_length=100, blank=True, null=True)
    img3_address = models.CharField(max_length=100, blank=True, null=True)
    img4_address = models.CharField(max_length=100, blank=True, null=True)
    img5_address = models.CharField(max_length=100, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)
    key_words = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_other_perfume'


class ProductPerfume(models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    my_category = models.CharField(max_length=60, blank=True, null=True)
    platform = models.CharField(max_length=60, blank=True, null=True)
    first_category = models.CharField(max_length=30, blank=True, null=True)
    third_category = models.CharField(max_length=30, blank=True, null=True)
    second_category = models.CharField(max_length=30, blank=True, null=True)
    img1_address = models.CharField(max_length=255, blank=True, null=True)
    img2_address = models.CharField(max_length=255, blank=True, null=True)
    img3_address = models.CharField(max_length=255, blank=True, null=True)
    img4_address = models.CharField(max_length=255, blank=True, null=True)
    img5_address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=50, blank=True, null=True)
    new_comment_count = models.CharField(max_length=50, blank=True, null=True)
    kg = models.CharField(max_length=255, blank=True, null=True)
    good_for_who = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    who_handly = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.DateTimeField(blank=True, null=True)
    finish_get_data = models.IntegerField(blank=True, null=True)
    store = models.CharField(max_length=60, blank=True, null=True)
    clean_weight = models.CharField(max_length=60, blank=True, null=True)
    package = models.CharField(max_length=60, blank=True, null=True)
    fragrance = models.CharField(max_length=60, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    fragrance_type = models.CharField(max_length=255, blank=True, null=True)
    key_words = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_perfume'


class UserCutPriceProduct(models.Model):
    product_address = models.CharField(max_length=255, blank=True, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_platform = models.CharField(max_length=255, blank=True, null=True)
    product_comment_count = models.CharField(max_length=255, blank=True, null=True)
    user_phone = models.CharField(max_length=20, blank=True, null=True)
    product_img_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_cut_price_product'


class Users(models.Model):
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=40, blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class VipProductLipstick(models.Model):
    first_category = models.CharField(max_length=30, blank=True, null=True)
    third_category = models.CharField(max_length=30, blank=True, null=True)
    second_category = models.CharField(max_length=30, blank=True, null=True)
    img1_address = models.CharField(max_length=255, blank=True, null=True)
    img2_address = models.CharField(max_length=255, blank=True, null=True)
    img3_address = models.CharField(max_length=255, blank=True, null=True)
    img4_address = models.CharField(max_length=255, blank=True, null=True)
    img5_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=255, blank=True, null=True)
    kg = models.CharField(max_length=255, blank=True, null=True)
    good_for_who = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    makeup_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    who_handly = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    v_sku_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vip_product_lipstick'


class VipProductLipstickCopy(models.Model):
    first_category = models.CharField(max_length=30, blank=True, null=True)
    third_category = models.CharField(max_length=30, blank=True, null=True)
    second_category = models.CharField(max_length=30, blank=True, null=True)
    img1_address = models.CharField(max_length=255, blank=True, null=True)
    img2_address = models.CharField(max_length=255, blank=True, null=True)
    img3_address = models.CharField(max_length=255, blank=True, null=True)
    img4_address = models.CharField(max_length=255, blank=True, null=True)
    img5_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    produce_address = models.CharField(max_length=255, blank=True, null=True)
    comment_count = models.CharField(max_length=255, blank=True, null=True)
    kg = models.CharField(max_length=255, blank=True, null=True)
    good_for_who = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    result_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    makeup_effectiveness = models.CharField(max_length=255, blank=True, null=True)
    good_comment_percentage = models.CharField(max_length=255, blank=True, null=True)
    who_handly = models.CharField(max_length=255, blank=True, null=True)
    get_time = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    v_sku_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vip_product_lipstick_copy'
