package com.example.alarmapp;

  import android.app.Service;
  import android.content.Intent;
  import android.os.IBinder;
  import android.app.AlarmManager;
  import android.app.PendingIntent;
  import android.content.Context;
  import java.util.Calendar;

  public class AlarmService extends Service {
      @Override
      public int onStartCommand(Intent intent, int flags, int startId) {
          // الحصول على الوقت من Intent
          String time = intent.getStringExtra("alarm_time");
          String[] timeParts = time.split(":");
          int hour = Integer.parseInt(timeParts[0]);
          int minute = Integer.parseInt(timeParts[1]);

          // جدولة المنبه
          AlarmManager alarmManager = (AlarmManager) getSystemService(Context.ALARM_SERVICE);
          Intent alarmIntent = new Intent(this, AlarmReceiver.class);
          PendingIntent pendingIntent = PendingIntent.getBroadcast(this, 0, alarmIntent, PendingIntent.FLAG_UPDATE_CURRENT);

          Calendar calendar = Calendar.getInstance();
          calendar.set(Calendar.HOUR_OF_DAY, hour);
          calendar.set(Calendar.MINUTE, minute);
          calendar.set(Calendar.SECOND, 0);

          alarmManager.setExact(AlarmManager.RTC_WAKEUP, calendar.getTimeInMillis(), pendingIntent);

          return START_STICKY;
      }

      @Override
      public IBinder onBind(Intent intent) {
          return null;
      }
  }