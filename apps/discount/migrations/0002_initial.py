# Generated by Django 4.1.5 on 2023-02-12 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0003_initial'),
        ('discount', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discountconditionproducttype',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='product.producttype'),
        ),
        migrations.AddField(
            model_name='discountconditionproducttag',
            name='discount_condition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='discount.discountcondition'),
        ),
        migrations.AddField(
            model_name='discountconditionproducttag',
            name='product_tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.producttag'),
        ),
        migrations.AddField(
            model_name='discountconditionproductcollection',
            name='discount_condition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discount.discountcondition'),
        ),
        migrations.AddField(
            model_name='discountconditionproductcollection',
            name='product_collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productcollection'),
        ),
        migrations.AddField(
            model_name='discountconditionproduct',
            name='discount_condition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='discount.discountcondition'),
        ),
        migrations.AddField(
            model_name='discountconditionproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='product.product'),
        ),
        migrations.AddField(
            model_name='discountconditioncustomergroup',
            name='customer_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customergroup'),
        ),
        migrations.AddField(
            model_name='discountconditioncustomergroup',
            name='discount_condition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discount.discountcondition'),
        ),
        migrations.AddField(
            model_name='discountcondition',
            name='customer_groups',
            field=models.ManyToManyField(through='discount.DiscountConditionCustomerGroup', to='customer.customergroup'),
        ),
        migrations.AddField(
            model_name='discountcondition',
            name='discount_rule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='discount.discountrule'),
        ),
        migrations.AddField(
            model_name='discountcondition',
            name='product_collections',
            field=models.ManyToManyField(through='discount.DiscountConditionProductCollection', to='product.productcollection'),
        ),
        migrations.AddField(
            model_name='discountcondition',
            name='product_tags',
            field=models.ManyToManyField(through='discount.DiscountConditionProductTag', to='product.producttag'),
        ),
        migrations.AddField(
            model_name='discountcondition',
            name='product_types',
            field=models.ManyToManyField(through='discount.DiscountConditionProductType', to='product.producttype'),
        ),
        migrations.AddField(
            model_name='discountcondition',
            name='products',
            field=models.ManyToManyField(through='discount.DiscountConditionProduct', to='product.product'),
        ),
        migrations.AddField(
            model_name='discount',
            name='parent_discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='discount.discount'),
        ),
        migrations.AddField(
            model_name='discount',
            name='regions',
            field=models.ManyToManyField(related_name='+', to='customer.region'),
        ),
        migrations.AddField(
            model_name='discount',
            name='rule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='discount.discountrule'),
        ),
        migrations.AlterUniqueTogether(
            name='discountconditionproducttype',
            unique_together={('product_type', 'discount_condition')},
        ),
        migrations.AlterUniqueTogether(
            name='discountconditionproduct',
            unique_together={('product', 'discount_condition')},
        ),
    ]
