#Задача 1: Проверка пароля (Основы языка Java, операторы, ветвления)

# Создайте класс PasswordVerifier. Этот класс должен содержать метод, который принимает строку пароля и проверяет его на соответствие следующим правилам:
#
# Пароль должен быть не менее 8 символов.
# Пароль должен содержать хотя бы одну цифру.
# Пароль должен содержать хотя бы одну заглавную букву.
# Метод должен выбрасывать исключение, если пароль не соответствует какому-либо из этих правил.
  
class PasswordVerifier:
    def __init__(self, pas: str):
        self.password = pas
        self.verification = False
        self.verifier()
        self.result()

    def verifier(self):
        try:
            if len(self.password) > 7:
                if any(map(str.isdigit, self.password)):
                    if any(map(str.isupper, self.password)):
                        self.verification = True
                    else: raise error_my("Проверка на заглавные буквы провалена")
                else: raise error_my("проверка на цифры не проедена")
            else:
                raise error_my("Длина пароля менее 8 символов")
        except error_my as e:
                print("Ошибка:", e.message)

    def result(self):
        return self.verification

class error_my(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

if __name__ == '__main__':
    p = PasswordVerifier("asfeegjk")
