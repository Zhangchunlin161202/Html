# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-04 02:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerCare',
            fields=[
                ('care_id', models.AutoField(primary_key=True, serialize=False)),
                ('care_theme', models.CharField(blank=True, max_length=50, null=True)),
                ('care_way', models.CharField(blank=True, max_length=50, null=True)),
                ('care_time', models.DateTimeField()),
                ('care_remark', models.CharField(blank=True, max_length=1000, null=True)),
                ('care_nexttime', models.DateTimeField()),
                ('care_people', models.CharField(blank=True, max_length=50, null=True)),
                ('is_used', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'customer_care',
            },
        ),
        migrations.CreateModel(
            name='CustomerCondition',
            fields=[
                ('condition_id', models.AutoField(primary_key=True, serialize=False)),
                ('condition_name', models.CharField(blank=True, max_length=50, null=True)),
                ('condition_explain', models.CharField(blank=True, max_length=1000, null=True)),
                ('is_used', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'customer_condition',
            },
        ),
        migrations.CreateModel(
            name='CustomerInfo',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_sex', models.CharField(blank=True, max_length=10, null=True)),
                ('customer_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_qq', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_address', models.CharField(blank=True, max_length=500, null=True)),
                ('customer_email', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_remark', models.CharField(blank=True, max_length=1000, null=True)),
                ('customer_job', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_blog', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_tel', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_msn', models.CharField(blank=True, max_length=50, null=True)),
                ('birth_day', models.DateTimeField()),
                ('customer_addtime', models.DateTimeField()),
                ('customer_addman', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_changtime', models.DateTimeField()),
                ('change_man', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_company', models.CharField(blank=True, max_length=50, null=True)),
                ('is_used', models.CharField(blank=True, max_length=10, null=True)),
                ('condition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employee.CustomerCondition')),
            ],
            options={
                'db_table': 'customer_info',
            },
        ),
        migrations.CreateModel(
            name='CustomerLinkman',
            fields=[
                ('linkman_id', models.AutoField(primary_key=True, serialize=False)),
                ('linkman_name', models.CharField(blank=True, max_length=50, null=True)),
                ('linkman_sex', models.CharField(blank=True, max_length=20, null=True)),
                ('linkman_job', models.CharField(blank=True, max_length=100, null=True)),
                ('linkman_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('linkman_age', models.IntegerField(blank=True, null=True)),
                ('linkman_relation', models.CharField(blank=True, max_length=50, null=True)),
                ('is_used', models.CharField(blank=True, max_length=10, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employee.CustomerInfo')),
            ],
            options={
                'db_table': 'customer_linkman',
            },
        ),
        migrations.CreateModel(
            name='CustomerLinkreord',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('link_time', models.DateTimeField()),
                ('who_link', models.CharField(blank=True, max_length=50, null=True)),
                ('link_type', models.CharField(blank=True, max_length=50, null=True)),
                ('link_theme', models.CharField(blank=True, max_length=200, null=True)),
                ('link_nexttime', models.DateTimeField()),
                ('link_remark', models.CharField(blank=True, max_length=1000, null=True)),
                ('is_used', models.CharField(blank=True, max_length=10, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employee.CustomerInfo')),
            ],
            options={
                'db_table': 'customer_linkreord',
            },
        ),
        migrations.CreateModel(
            name='CustomerSource',
            fields=[
                ('source_id', models.AutoField(primary_key=True, serialize=False)),
                ('source_name', models.CharField(blank=True, max_length=50, null=True)),
                ('is_used', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'customer_source',
            },
        ),
        migrations.CreateModel(
            name='CustomerType',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(blank=True, max_length=50, null=True)),
                ('is_used', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'customer_type',
            },
        ),
        migrations.CreateModel(
            name='DepartmentInfo',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(blank=True, max_length=50, null=True)),
                ('department_desc', models.CharField(blank=True, max_length=500, null=True)),
                ('is_used', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'department_info',
            },
        ),
        migrations.CreateModel(
            name='DetailInfo',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False, verbose_name='\u5e8f\u53f7')),
                ('s_name', models.CharField(max_length=100, verbose_name='\u59d3\u540d')),
                ('s_age', models.CharField(max_length=100, verbose_name='\u5e74\u9f84')),
                ('s_gender', models.CharField(max_length=100, verbose_name='\u6027\u522b')),
                ('s_education', models.CharField(max_length=100, verbose_name='\u5b66\u5386')),
                ('s_section', models.CharField(max_length=100, verbose_name='\u90e8\u95e8')),
                ('s_call', models.CharField(max_length=100, verbose_name='\u7535\u8bdd')),
                ('s_paycard', models.CharField(max_length=100, verbose_name='\u5de5\u8d44\u5361\u53f7')),
                ('s_card', models.CharField(max_length=100, verbose_name='\u8eab\u4efd\u8bc1')),
                ('s_created', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('s_edi_created', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('s_add_people', models.CharField(max_length=100, verbose_name='\u6dfb\u52a0\u4eba')),
                ('s_edi_people', models.CharField(max_length=100, verbose_name='\u4fee\u6539\u4eba')),
                ('s_role', models.CharField(max_length=100, verbose_name='\u89d2\u8272')),
                ('s_account', models.CharField(max_length=100, verbose_name='\u8d26\u53f7')),
                ('s_password', models.CharField(max_length=100, verbose_name='\u5bc6\u7801')),
                ('s_nation', models.CharField(max_length=100, verbose_name='\u6c11\u65cf')),
                ('s_marriage', models.CharField(max_length=100, verbose_name='\u5a5a\u59fb')),
                ('s_power', models.CharField(max_length=100, verbose_name='\u6743\u9650')),
                ('s_phone', models.CharField(max_length=100, verbose_name='\u624b\u673a')),
                ('s_addres', models.CharField(max_length=100, verbose_name='\u5bb6\u5ead\u5730\u5740')),
                ('s_hobby', models.CharField(max_length=1000, verbose_name='\u7231\u597d')),
                ('s_email', models.CharField(max_length=100, verbose_name='\u90ae\u7bb1')),
            ],
            options={
                'db_table': 't_DetailInfo',
                'verbose_name_plural': '\u7f16\u8f91',
            },
        ),
        migrations.CreateModel(
            name='EmailInfo',
            fields=[
                ('email_id', models.AutoField(primary_key=True, serialize=False)),
                ('email_content', models.CharField(blank=True, max_length=2000, null=True)),
                ('email_time', models.DateTimeField()),
                ('email_state', models.CharField(blank=True, max_length=50, null=True)),
                ('email_theme', models.CharField(blank=True, max_length=200, null=True)),
                ('is_used', models.CharField(blank=True, max_length=10, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employee.CustomerInfo')),
            ],
            options={
                'db_table': 'email_info',
            },
        ),
        migrations.CreateModel(
            name='HouseInfo',
            fields=[
                ('house_id', models.AutoField(primary_key=True, serialize=False)),
                ('house_address', models.CharField(blank=True, max_length=500, null=True)),
                ('house_price', models.IntegerField(blank=True, null=True)),
                ('house_ambient', models.CharField(blank=True, max_length=1000, null=True)),
                ('is_used', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'house_info',
            },
        ),
        migrations.CreateModel(
            name='HouseType',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(blank=True, max_length=50, null=True)),
                ('is_used', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'house_type',
            },
        ),
        migrations.CreateModel(
            name='NoticeInfo',
            fields=[
                ('notice_id', models.AutoField(primary_key=True, serialize=False)),
                ('notice_item', models.CharField(blank=True, max_length=100, null=True)),
                ('notice_content', models.CharField(blank=True, max_length=2000, null=True)),
                ('notice_time', models.DateTimeField()),
                ('notice_endtime', models.DateTimeField()),
                ('is_used', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'notice_info',
            },
        ),
        migrations.CreateModel(
            name='StaffInfo',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(max_length=100, unique=True, verbose_name='\u59d3\u540d')),
                ('s_gender', models.CharField(max_length=100, verbose_name='\u6027\u522b')),
                ('s_years', models.CharField(max_length=100, verbose_name='\u5e74\u9f84')),
                ('s_nation', models.CharField(max_length=100, verbose_name='\u6c11\u65cf')),
                ('s_section', models.CharField(max_length=100, verbose_name='\u90e8\u95e8')),
                ('s_role', models.CharField(max_length=100, verbose_name='\u89d2\u8272')),
                ('s_education', models.CharField(max_length=100, verbose_name='\u5b66\u5386')),
                ('s_marriage', models.CharField(max_length=100, verbose_name='\u5a5a\u59fb')),
                ('s_addr', models.CharField(max_length=100, verbose_name='\u5bb6\u5ead\u5730\u5740')),
                ('s_phone', models.CharField(max_length=100, verbose_name='\u624b\u673a')),
                ('s_call', models.CharField(max_length=100, verbose_name='\u7535\u8bdd')),
                ('s_email', models.CharField(max_length=100, verbose_name='\u90ae\u7bb1')),
            ],
            options={
                'db_table': 't_StaffInfo',
                'verbose_name_plural': '\u5458\u5de5\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, max_length=50, null=True)),
                ('user_sex', models.CharField(blank=True, max_length=10, null=True)),
                ('user_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('user_age', models.IntegerField(blank=True, null=True)),
                ('user_address', models.CharField(blank=True, max_length=500, null=True)),
                ('user_num', models.CharField(blank=True, max_length=100, null=True)),
                ('user_pw', models.CharField(blank=True, max_length=50, null=True)),
                ('user_tel', models.CharField(blank=True, max_length=20, null=True)),
                ('user_idnum', models.CharField(blank=True, max_length=20, null=True)),
                ('user_email', models.CharField(blank=True, max_length=100, null=True)),
                ('user_addtime', models.DateTimeField(auto_now_add=True)),
                ('user_addman', models.CharField(blank=True, max_length=50, null=True)),
                ('user_changetime', models.DateTimeField(auto_now=True)),
                ('user_changeman', models.CharField(blank=True, max_length=50, null=True)),
                ('user_intest', models.CharField(blank=True, max_length=1000, null=True)),
                ('user_diploma', models.CharField(blank=True, max_length=20, null=True)),
                ('user_bankcard', models.CharField(blank=True, max_length=20, null=True)),
                ('user_nation', models.CharField(blank=True, max_length=20, null=True)),
                ('is_married', models.CharField(blank=True, max_length=10, null=True)),
                ('is_used', models.CharField(blank=True, max_length=10, null=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employee.DepartmentInfo')),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(blank=True, max_length=50, null=True)),
                ('role_power', models.IntegerField(blank=True, null=True)),
                ('is_used', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'user_role',
            },
        ),
        migrations.AddField(
            model_name='userinfo',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employee.UserRole'),
        ),
        migrations.AddField(
            model_name='noticeinfo',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employee.UserInfo'),
        ),
        migrations.AddField(
            model_name='houseinfo',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employee.HouseType'),
        ),
        migrations.AddField(
            model_name='houseinfo',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employee.UserInfo'),
        ),
        migrations.AddField(
            model_name='emailinfo',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employee.UserInfo'),
        ),
        migrations.AddField(
            model_name='customerinfo',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employee.CustomerSource'),
        ),
        migrations.AddField(
            model_name='customerinfo',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employee.CustomerType'),
        ),
        migrations.AddField(
            model_name='customerinfo',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employee.UserInfo'),
        ),
        migrations.AddField(
            model_name='customercare',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employee.CustomerInfo'),
        ),
    ]
