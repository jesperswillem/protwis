# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-06 14:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('protein', '0003_auto_20160426_1319'),
        ('ligand', '0001_initial'),
        ('structure', '0001_initial'),
        ('construct', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChemicalListName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'construct_chemical_list_name',
            },
        ),
        migrations.CreateModel(
            name='Construct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, unique=True)),
                ('json', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConstructModification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modification', models.TextField(max_length=50)),
                ('position_type', models.TextField(max_length=20)),
                ('pos_start', models.SmallIntegerField()),
                ('pos_end', models.SmallIntegerField()),
                ('remark', models.TextField()),
            ],
            options={
                'db_table': 'construct_modification',
            },
        ),
        migrations.CreateModel(
            name='ContributorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('pi_email', models.TextField(max_length=50)),
                ('pi_name', models.TextField(max_length=50)),
                ('urls', models.TextField()),
                ('date', models.DateField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CrystalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolution', models.DecimalField(decimal_places=3, max_digits=5)),
                ('pdb_code', models.TextField(max_length=10, null=True)),
                ('pdb_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='structure.PdbData')),
            ],
        ),
        migrations.CreateModel(
            name='CrystallizationMethods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'construct_crystallization_methods',
            },
        ),
        migrations.CreateModel(
            name='CrystallizationTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sub_name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'construct_crystallization_types',
            },
        ),
        migrations.RemoveField(
            model_name='chemicalmodification',
            name='construct_solubilization',
        ),
        migrations.RemoveField(
            model_name='expression',
            name='construct',
        ),
        migrations.RemoveField(
            model_name='expression',
            name='expression_system',
        ),
        migrations.RemoveField(
            model_name='constructdeletion',
            name='construct',
        ),
        migrations.RemoveField(
            model_name='constructinsertion',
            name='construct',
        ),
        migrations.RemoveField(
            model_name='constructinsertion',
            name='deletions',
        ),
        migrations.RemoveField(
            model_name='constructinsertion',
            name='name',
        ),
        migrations.RemoveField(
            model_name='constructinsertion',
            name='protein_type',
        ),
        migrations.RemoveField(
            model_name='constructinsertion',
            name='sequence',
        ),
        migrations.RemoveField(
            model_name='constructinsertion',
            name='uniprot_id',
        ),
        migrations.RemoveField(
            model_name='constructmutation',
            name='construct',
        ),
        migrations.RemoveField(
            model_name='crystallization',
            name='aqueous_solution_lipid_ratio',
        ),
        migrations.RemoveField(
            model_name='crystallization',
            name='chemical_list',
        ),
        migrations.RemoveField(
            model_name='crystallization',
            name='construct',
        ),
        migrations.RemoveField(
            model_name='crystallization',
            name='lcp_bolus_volume',
        ),
        migrations.RemoveField(
            model_name='crystallization',
            name='method',
        ),
        migrations.RemoveField(
            model_name='crystallization',
            name='ph',
        ),
        migrations.RemoveField(
            model_name='crystallization',
            name='precipitant_solution_volume',
        ),
        migrations.RemoveField(
            model_name='crystallization',
            name='settings',
        ),
        migrations.RemoveField(
            model_name='crystallizationligandconc',
            name='construct_crystallization',
        ),
        migrations.RemoveField(
            model_name='purification',
            name='construct',
        ),
        migrations.RemoveField(
            model_name='purificationstep',
            name='purification',
        ),
        migrations.RemoveField(
            model_name='purificationstep',
            name='purification_type',
        ),
        migrations.RemoveField(
            model_name='solubilization',
            name='construct',
        ),
        migrations.RemoveField(
            model_name='crystallization',
            name='ligands',
        ),
        migrations.RemoveField(
            model_name='chemicalconc',
            name='concentration',
        ),
        migrations.RemoveField(
            model_name='crystallization',
            name='protein_conc',
        ),
        migrations.RemoveField(
            model_name='crystallization',
            name='temp',
        ),
        migrations.RemoveField(
            model_name='crystallizationligandconc',
            name='ligand_conc',
        ),
        migrations.AddField(
            model_name='chemicalconc',
            name='concentration_unit',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='constructinsertion',
            name='end',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='constructinsertion',
            name='insert_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='construct.ConstructInsertionType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='constructinsertion',
            name='presence',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='constructinsertion',
            name='start',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='constructinsertiontype',
            name='sequence',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='constructinsertiontype',
            name='subtype',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='crystallization',
            name='chemical_lists',
            field=models.ManyToManyField(to='construct.ChemicalList'),
        ),
        migrations.AddField(
            model_name='crystallization',
            name='ph_end',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crystallization',
            name='ph_start',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crystallization',
            name='protein_conc_unit',
            field=models.TextField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='crystallizationligandconc',
            name='ligand_conc_unit',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='crystallizationligandconc',
            name='ligand_role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ligand.LigandRole'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expressionsystem',
            name='remarks',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='purification',
            name='steps',
            field=models.ManyToManyField(to='construct.PurificationStep'),
        ),
        migrations.AddField(
            model_name='purificationstep',
            name='name',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chemicalconc',
            name='concentration',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='chemicaltype',
            name='name',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='crystallization',
            name='crystal_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='construct.CrystallizationTypes'),
        ),
        migrations.AddField(
            model_name='crystallization',
            name='ligands',
            field=models.ManyToManyField(to='construct.CrystallizationLigandConc'),
        ),
        migrations.AddField(
            model_name='crystallization',
            name='protein_conc',
            field=models.FloatField(),
        ),
        migrations.AddField(
            model_name='crystallization',
            name='temp',
            field=models.FloatField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crystallizationligandconc',
            name='ligand_conc',
            field=models.FloatField(),
        ),
        migrations.AlterUniqueTogether(
            name='chemical',
            unique_together=set([('name', 'chemical_type')]),
        ),
        migrations.DeleteModel(
            name='ChemicalModification',
        ),
        migrations.DeleteModel(
            name='CrystallizationMethodTypes',
        ),
        migrations.DeleteModel(
            name='Expression',
        ),
        migrations.DeleteModel(
            name='PurificationStepType',
        ),
        migrations.AddField(
            model_name='construct',
            name='contributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construct.ContributorInfo'),
        ),
        migrations.AddField(
            model_name='construct',
            name='crystal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='construct.CrystalInfo'),
        ),
        migrations.AddField(
            model_name='construct',
            name='crystallization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='construct.Crystallization'),
        ),
        migrations.AddField(
            model_name='construct',
            name='deletions',
            field=models.ManyToManyField(to='construct.ConstructDeletion'),
        ),
        migrations.AddField(
            model_name='construct',
            name='expression',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='construct.ExpressionSystem'),
        ),
        migrations.AddField(
            model_name='construct',
            name='insertions',
            field=models.ManyToManyField(to='construct.ConstructInsertion'),
        ),
        migrations.AddField(
            model_name='construct',
            name='modifications',
            field=models.ManyToManyField(to='construct.ConstructModification'),
        ),
        migrations.AddField(
            model_name='construct',
            name='mutations',
            field=models.ManyToManyField(to='construct.ConstructMutation'),
        ),
        migrations.AddField(
            model_name='construct',
            name='protein',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protein.Protein'),
        ),
        migrations.AddField(
            model_name='construct',
            name='purification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='construct.Purification'),
        ),
        migrations.AddField(
            model_name='construct',
            name='solubilization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='construct.Solubilization'),
        ),
        migrations.AddField(
            model_name='chemicallist',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='construct.ChemicalListName'),
        ),
        migrations.AddField(
            model_name='crystallization',
            name='crystal_method',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='construct.CrystallizationMethods'),
        ),
    ]
