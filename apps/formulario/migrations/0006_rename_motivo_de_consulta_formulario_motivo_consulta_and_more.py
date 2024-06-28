# Generated by Django 4.2.7 on 2024-06-27 16:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("formulario", "0005_formulario_ptnm_pm_formulario_ptnm_pn_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="formulario",
            old_name="motivo_de_consulta",
            new_name="motivo_consulta",
        ),
        migrations.AlterField(
            model_name="formulario",
            name="dosis_total",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0,
                max_digits=15,
                null=True,
                verbose_name="Dosis total",
            ),
        ),
        migrations.AlterField(
            model_name="formulario",
            name="ptnm_pM",
            field=models.CharField(
                blank=True, max_length=256, null=True, verbose_name="pTNM pM"
            ),
        ),
        migrations.AlterField(
            model_name="formulario",
            name="ptnm_pN",
            field=models.CharField(
                blank=True, max_length=256, null=True, verbose_name="pTNM pN"
            ),
        ),
        migrations.AlterField(
            model_name="formulario",
            name="ptnm_pT",
            field=models.CharField(
                blank=True, max_length=256, null=True, verbose_name="pTNM pT"
            ),
        ),
    ]
