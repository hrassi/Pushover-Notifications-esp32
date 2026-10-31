# ============================================================
# PushOver Notification
# ============================================================


import sys
import gc

def pushover(title, message):
    try:
        import pushover_notification

        return pushover_notification.send_notification(
            title, message
        )

    except Exception as e:
        print("[Pushover] Error:", e)
        return False

    finally:
        sys.modules.pop("pushover_notification", None)

        try:
            del pushover_notification
        except NameError:
            pass

        gc.collect()
        
        
#### whenever you want to send pushover notification :
        
pushover("ESP4 Heater","Temperature too high!")

        
        