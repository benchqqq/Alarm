package com.example.alarmapp;

  import android.content.BroadcastReceiver;
  import android.content.Context;
  import android.content.Intent;
  import android.media.Ringtone;
  import android.media.RingtoneManager;
  import android.net.Uri;

  public class AlarmReceiver extends BroadcastReceiver {
      @Override
      public void onReceive(Context context, Intent intent) {
          // تشغيل صوت التنبيه
          Uri alarmUri = RingtoneManager.getDefaultUri(RingtoneManager.TYPE_ALARM);
          if (alarmUri == null) {
              alarmUri = RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION);
          }
          Ringtone ringtone = RingtoneManager.getRingtone(context, alarmUri);
          ringtone.play();
      }
  }