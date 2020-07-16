from django.http import HttpResponse
import RPi.GPIO as GPIO

LED_PIN = 24


def turnOn(request):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, 1)
    html = "<html><body>Turn On.</body></html>"
    return HttpResponse(html)


def turnOff(request):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, 0)
    html = "<html><body>Turn Off.</body></html>"
    return HttpResponse(html)