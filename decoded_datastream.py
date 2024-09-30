import base64
import json


kinesis_event = {
    "SequenceNumber": "49656251968795993543920822232486532584175433385649373186",
    "ApproximateArrivalTimestamp": "2024-09-29T15:53:16.603000+00:00",
    "Data": "eyJFdmVudElkIjoxLCJEZXNjcmlwdGlvbiI6IlByb2Nlc3MgQ3JlYXRlOlxyXG5SdWxlTmFtZTogLVxyXG5VdGNUaW1lOiAyMDI0LTA5LTI5IDE1OjUzOjE0LjEzMVxyXG5Qcm9jZXNzR3VpZDogezVmNzFiZWYxLTc3ZWEtNjZmOS1hZjA1LTAwMDAwMDAwMWUwMX1cclxuUHJvY2Vzc0lkOiA3MzcyXHJcbkltYWdlOiBDOlxcV2luZG93c1xcU3lzdGVtMzJcXHdiZW1cXFdtaVBydlNFLmV4ZVxyXG5GaWxlVmVyc2lvbjogMTAuMC4yMDM0OC4xIChXaW5CdWlsZC4xNjAxMDEuMDgwMClcclxuRGVzY3JpcHRpb246IFdNSSBQcm92aWRlciBIb3N0XHJcblByb2R1Y3Q6IE1pY3Jvc29mdMKuIFdpbmRvd3PCriBPcGVyYXRpbmcgU3lzdGVtXHJcbkNvbXBhbnk6IE1pY3Jvc29mdCBDb3Jwb3JhdGlvblxyXG5PcmlnaW5hbEZpbGVOYW1lOiBXbWlwcnZzZS5leGVcclxuQ29tbWFuZExpbmU6IEM6XFxXaW5kb3dzXFxzeXN0ZW0zMlxcd2JlbVxcd21pcHJ2c2UuZXhlIC1zZWN1cmVkIC1FbWJlZGRpbmdcclxuQ3VycmVudERpcmVjdG9yeTogQzpcXFdpbmRvd3NcXHN5c3RlbTMyXFxcclxuVXNlcjogTlQgQVVUSE9SSVRZXFxORVRXT1JLIFNFUlZJQ0VcclxuTG9nb25HdWlkOiB7NWY3MWJlZjEtMTc1OS02NmY3LWU0MDMtMDAwMDAwMDAwMDAwfVxyXG5Mb2dvbklkOiAweDNFNFxyXG5UZXJtaW5hbFNlc3Npb25JZDogMFxyXG5JbnRlZ3JpdHlMZXZlbDogU3lzdGVtXHJcbkhhc2hlczogU0hBMjU2PTE3OTI3MzFFMDMwQjdGRTM1QTdFQjIxQzlGOTA3RUFFNkU0QUMzODFERTkxODAwM0YyNzA5MTg1QzRDRTBBNUFcclxuUGFyZW50UHJvY2Vzc0d1aWQ6IHs1ZjcxYmVmMS0xNzU5LTY2ZjctMGQwMC0wMDAwMDAwMDFlMDF9XHJcblBhcmVudFByb2Nlc3NJZDogOTkyXHJcblBhcmVudEltYWdlOiBDOlxcV2luZG93c1xcU3lzdGVtMzJcXHN2Y2hvc3QuZXhlXHJcblBhcmVudENvbW1hbmRMaW5lOiBDOlxcV2luZG93c1xcc3lzdGVtMzJcXHN2Y2hvc3QuZXhlIC1rIERjb21MYXVuY2ggLXBcclxuUGFyZW50VXNlcjogTlQgQVVUSE9SSVRZXFxTWVNURU0iLCJMZXZlbERpc3BsYXlOYW1lIjoiSW5mb3JtYXRpb25hbCIsIkxvZ05hbWUiOiJNaWNyb3NvZnQtV2luZG93cy1TeXNtb24vT3BlcmF0aW9uYWwiLCJNYWNoaW5lTmFtZSI6IkRDMDEub2plZGFsZW9uYXJkby5sb2NhbCIsIlByb3ZpZGVyTmFtZSI6Ik1pY3Jvc29mdC1XaW5kb3dzLVN5c21vbiIsIlRpbWVDcmVhdGVkIjoiMjAyNC0wOS0yOVQxNTo1MzoxNC4xMzI5OTU4WiIsIkluZGV4Ijo3OTMyLCJVc2VyTmFtZSI6IlMtMS01LTE4IiwiS2V5d29yZHMiOiIiLCJob3N0IjoiREMwMSJ9Cg==",
    "PartitionKey": "46821,41684313371",
    "EncryptionType": "KMS"
}

decoded_data = base64.b64decode(kinesis_event["Data"]).decode('utf-8')
json_data = json.loads(decoded_data)
print(json.dumps(json_data, indent=4))
