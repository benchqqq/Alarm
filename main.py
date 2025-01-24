import flet as ft
from jnius import autoclass

def main(page: ft.Page):
    # إعدادات الصفحة
    page.title = "تطبيق المنبه"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = ft.colors.BLUE_GREY_100
    page.padding = 20

    # حقل إدخال الوقت
    time_input = ft.TextField(
        label="أدخل وقت المنبه (HH:MM)",
        width=300,
        height=50,
        border_color=ft.colors.BLUE_700,
        text_size=18,
        color=ft.colors.BLUE_900,
    )

    # دالة تُنفذ عند النقر على الزر
    def set_alarm(e):
        try:
            # تحقق من صحة الوقت المدخل
            alarm_time = time_input.value
            Intent = autoclass('android.content.Intent')
            Context = autoclass('android.content.Context')
            AlarmService = autoclass('com.example.alarmapp.AlarmService')

            # إنشاء Intent
            intent = Intent(Context.ALARM_SERVICE)
            intent.setClass(Context, AlarmService)
            intent.putExtra("alarm_time", alarm_time)  # الوقت المطلوب

            # بدء الخدمة
            Context.startService(intent)

            page.add(ft.Text(value=f"تم ضبط المنبه لـ {alarm_time}", color=ft.colors.GREEN_900))
        except Exception as ex:
            page.add(ft.Text(value=f"حدث خطأ: {ex}", color=ft.colors.RED_900))

    # الزر
    set_alarm_button = ft.ElevatedButton(
        text="ضبط المنبه",
        on_click=set_alarm,
        bgcolor=ft.colors.BLUE_700,
        color=ft.colors.WHITE,
        width=200,
        height=50,
    )

    # إضافة العناصر إلى الصفحة
    page.add(
        ft.Column(
            [
                ft.Text(
                    value="تطبيق المنبه",
                    size=30,
                    weight="bold",
                    color=ft.colors.BLUE_900,
                ),
                ft.Text(
                    value="أدخل وقت المنبه واضغط على الزر لضبطه.",
                    size=18,
                    color=ft.colors.BLUE_800,
                ),
                time_input,
                set_alarm_button,
            ],
            alignment="center",
            spacing=20,
        )
    )

# تشغيل التطبيق
ft.app(target=main)