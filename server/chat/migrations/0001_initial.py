# Generated by Django 4.2.4 on 2023-11-08 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='chat-attachments')),
                ('file_name', models.CharField(blank=True, max_length=255, null=True)),
                ('file_size', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group_admin', models.ManyToManyField(related_name='group_admin_rooms', to='userprofile.userprofile')),
                ('group_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator_rooms', to='userprofile.userprofile')),
                ('group_moderator', models.ManyToManyField(related_name='group_moderator_rooms', to='userprofile.userprofile')),
                ('profile', models.ManyToManyField(related_name='profile_rooms', to='userprofile.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='GroupRoomMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, max_length=1000, null=True)),
                ('is_file', models.BooleanField(default=False)),
                ('is_read', models.BooleanField(default=False)),
                ('is_offer_attached', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attachment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachment_ws_room_messages', to='chat.chatattachment')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_ws_room_messages', to='userprofile.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction', models.CharField(choices=[('like', 'like'), ('love', 'love'), ('haha', 'haha'), ('wow', 'wow'), ('sad', 'sad'), ('angry', 'angry')], default='like', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_rooms', to='userprofile.userprofile')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partner_rooms', to='userprofile.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='RoomMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, max_length=1000, null=True)),
                ('is_file', models.BooleanField(default=False)),
                ('is_read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attachment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachment_room_messages', to='chat.chatattachment')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner_room_messages', to='userprofile.userprofile')),
                ('reactions', models.ManyToManyField(blank=True, related_name='reaction_room_messages', to='chat.reaction')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_messages', to='chat.room')),
            ],
        ),
        migrations.AddField(
            model_name='reaction',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message_reactions', to='chat.roommessage'),
        ),
        migrations.AddField(
            model_name='reaction',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_reactions', to='userprofile.userprofile'),
        ),
        migrations.AddField(
            model_name='reaction',
            name='room_message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_message_reactions', to='chat.grouproommessage'),
        ),
        migrations.CreateModel(
            name='OnlineUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_id', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='online_profile', to='userprofile.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='grouproommessage',
            name='reactions',
            field=models.ManyToManyField(blank=True, related_name='reaction_ws_room_messages', to='chat.reaction'),
        ),
        migrations.AddField(
            model_name='grouproommessage',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ws_room_messages', to='chat.grouproom'),
        ),
    ]
