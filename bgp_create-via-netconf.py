from ncclient import manager
import device_info
import xmltodict
import xml.dom.minidom
"""
   This is a template to create bgp peer and configration
   using YANG data model driven programmability
"""
bgp = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <router>
        <bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-bgp">
          <id>100</id>
          <bgp>
            <log-neighbor-changes />
          </bgp>
          <neighbor>
            <id>1.2.3.4</id>
            <remote-as>200</remote-as>
            <route-map>
              <inout>in</inout>
              <route-map-name>RM-IN</route-map-name>
            </route-map>
            <route-map>
              <inout>out</inout>
              <route-map-name>RM-OUT</route-map-name>
            </route-map>
            <update-source>
              <Loopback>99</Loopback>
            </update-source>
          </neighbor>
        </bgp>
      </router>
    </native>
</config>
"""

with manager.connect(host="ios-xe-mgmt.cisco.com",
                     port=10000,
                     username='root',
                     password='D_Vay!_10&',
                     hostkey_verify=False) as m:


   bgp_config = m.edit_config(target = "running", config = bgp)
   #bgp_peer_xml=xml.dom.minidom.parseString(bgp_config.xml)
   #print(bgp_peer_xml.toprettyxml(indent = "  "))


           
