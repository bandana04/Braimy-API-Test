class AuthEndpoints:
    def __init__(self):
        self.register_user = '/tenant-auth/register'
        self.resend_otp = '/tenant-auth/resend-otp'
        self.verify_otp = '/tenant-auth/verify-otp'
        self.change_password = '/tenant-auth/refresh-token'
        self.forgot_password = '/tenant-auth/forgot-password'

