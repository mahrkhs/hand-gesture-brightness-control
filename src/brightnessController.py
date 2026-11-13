
import screen_brightness_control as sbc


class BrightnessController:

    def __init__(self, min_brightness=0, max_brightness=100):

        self.min_brightness = min_brightness
        self.max_brightness = max_brightness

        self.current_brightness = None

    def set_brightness(self, brightness):

        # Ensure brightness stays within the valid range
        brightness = int(
            max(
                self.min_brightness,
                min(self.max_brightness, brightness)
            )
        )

        # Avoid unnecessary brightness updates
        if brightness == self.current_brightness:
            return

        try:
            sbc.set_brightness(brightness)

            self.current_brightness = brightness

            return brightness

        except Exception as error:
            print(f"Brightness adjustment failed: {error}")
            return None

    def get_brightness(self):

        try:
            brightness = sbc.get_brightness()

            return brightness[0] if brightness else None

        except Exception as error:
            print(f"Could not retrieve brightness: {error}")
            return None
