from ncclient import manager
import device_info
import xmltodict
import xml.dom.minidom

prefix_list="""
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <ip>
        <prefix-list>
          <prefixes>
            <name>PL-IN</name>
            <seq>
              <no>5</no>
              <permit>
                <ip>192.168.68.0/24</ip>
              </permit>
            </seq>
          </prefixes>
          <prefixes>
            <name>PL-OUT</name>
            <seq>
              <no>5</no>
              <permit>
                <ip>172.16.0.0/16</ip>
              </permit>
            </seq>
          </prefixes>
        </prefix-list>
      </ip>
    </native>
</config>
"""

with manager.connect(host="ios-xe-mgmt.cisco.com",
                     port=10000,
                     username='root',
                     password='D_Vay!_10&',
                     hostkey_verify=False) as m:

   

   ip_prefix_list = m.edit_config(target = "running", config = prefix_list)
   #prefix_list_xml=xml.dom.minidom.parseString(ip_prefix_list.xml)
   #print(prefix_list_xml.toprettyxml(indent = "  "))


           
