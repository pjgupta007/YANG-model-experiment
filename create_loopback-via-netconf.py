from ncclient import manager
import device_info
import xmltodict
import xml.dom.minidom
"""
   This is a template to create loopback interface
   using YANG data model driven programmability
"""
create_loopback = """
<config>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
        <name>Loopback99</name>
        <description>Configured by PJ</description>
        <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
          ianaift:softwareLoopback
        </type>
        <enabled>true</enabled>
        <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
          <address>
            <ip>192.168.168.1</ip>
            <netmask>
              255.255.255.255
            </netmask>
          </address>
        </ipv4>
      </interface>
  </interfaces>
</config>
"""

with manager.connect(host="ios-xe-mgmt.cisco.com",
                     port=10000,
                     username='root',
                     password='D_Vay!_10&',
                     hostkey_verify=False) as m:


   loopback_config = m.edit_config(target = "running", config = create_loopback)
   #loopback_xml=xml.dom.minidom.parseString(loopback_config.xml)
   #print(loopback_xml.toprettyxml(indent = "  "))


           
