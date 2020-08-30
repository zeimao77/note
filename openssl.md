# 加密

## 摘要
 
- MD5
- SHA
- SHA-1

## 对称加密

- DES 
- 3DES 
- AES 

## 非对称加密 

- RSA 
- DSA 

##RSA 

```bash 
## 生成RSA密钥 
$ openssl rsautl --help
Usage: rsautl [options]
Valid options are:
 -help                    Display this summary
 -in infile               Input file
 -out outfile             Output file
 -inkey val               Input key
 -keyform PEM|DER|ENGINE  Private key format - default PEM
 -pubin                   Input is an RSA public
 -certin                  Input is a cert carrying an RSA public key
 -ssl                     Use SSL v2 padding
 -raw                     Use no padding
 -pkcs                    Use PKCS#1 v1.5 padding (default)
 -oaep                    Use PKCS#1 OAEP
 -sign                    Sign with private key
 -verify                  Verify with public key
 -asn1parse               Run output through asn1parse; useful with -verify
 -hexdump                 Hex dump output
 -x931                    Use ANSI X9.31 padding
 -rev                     Reverse the order of the input buffer
 -encrypt                 Encrypt with public key
 -decrypt                 Decrypt with private key
 -passin val              Input file pass phrase source
 -rand val                Load the file(s) into the random number generator
 -writerand outfile       Write random data to the specified file
 -engine val              Use engine, possibly a hardware device
## ===============================================================================
openssl genrsa -out private.pem 2048
## 生成公钥
openssl rsa -in private.pem -pubout -out public.pem
## 对文件加密
openssl rsautl -encrypt -in test.txt -inkey public.pem -pubin -out test.en
## 解密文件
openssl rsautl -decrypt -in test.en -inkey private.pem -out test.txt


## 签名
openssl dgst -sign private.pem -md5 -out test.sign test.txt
## 签名检验
openssl dgst -verify public.pem -md5 -signature test.sign test.txt
```

摘要
```bash 
## MD5摘要文件
openssl dgst -md5 test.txt 
## SHA1摘要文件 
openssl dgst -sha1 test.txt 
```