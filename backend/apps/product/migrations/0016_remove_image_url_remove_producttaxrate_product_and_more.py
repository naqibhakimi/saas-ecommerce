# Generated by Django 4.1.7 on 2023-08-07 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0015_product_origin_country"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="image",
            name="url",
        ),
        migrations.RemoveField(
            model_name="producttaxrate",
            name="product",
        ),
        migrations.RemoveField(
            model_name="productvariant",
            name="product",
        ),
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="product.moneyamount",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="tax_rate",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="product.producttaxrate",
            ),
        ),
        migrations.AddField(
            model_name="productcollection",
            name="products",
            field=models.ManyToManyField(to="product.product"),
        ),
        migrations.AddField(
            model_name="productvariant",
            name="inventory",
            field=models.ManyToManyField(to="product.productvariantinventoryitem"),
        ),
        migrations.AddField(
            model_name="productvariant",
            name="options",
            field=models.ManyToManyField(to="product.productoptionvalue"),
        ),
        migrations.RemoveField(
            model_name="product",
            name="category",
        ),
        migrations.RemoveField(
            model_name="product",
            name="collection",
        ),
        migrations.AlterField(
            model_name="product",
            name="tags",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="+", to="product.producttag"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="product.producttype",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="+", to="product.productcategory"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="collection",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="+", to="product.productcollection"
            ),
        ),
    ]
