from OpenSSL import crypto, SSL
from socket import gethostname
from pprint import pprint
from time import gmtime, mktime
from authlib.jose import jwk

import app.config as config

def create_self_signed_cert():

    # create a key pair
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 4096)

    # create a self-signed cert
    cert = crypto.X509()
    cert.get_subject().C = "DE"
    cert.get_subject().ST = "Internet"
    cert.get_subject().L = "Internet"
    cert.get_subject().O = "Mycelium Network"
    cert.get_subject().OU = config.ORGANIZATION_UNIT
    cert.get_subject().CN = config.APPLICATION_URL
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(365*24*60*60) # valid for 1 year
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha512')

    cert_dump = crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode("utf-8")
    private_key_dump = crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode("utf-8")
    public_key_dump = crypto.dump_publickey(crypto.FILETYPE_PEM, k).decode("utf-8")

    cert_file = open(config.CERT_FILE, "w")
    cert_file.write(cert_dump)
    cert_file.close()

    private_key_file = open(config.PRIVATE_KEY_FILE, "w")
    private_key_file.write(private_key_dump)
    private_key_file.close()

    public_key_file = open(config.PUBLIC_KEY_FILE, "w")
    public_key_file.write(public_key_dump)
    public_key_file.close()

    return cert_dump, private_key_dump, public_key_dump