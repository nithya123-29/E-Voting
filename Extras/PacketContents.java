import jpcap.PacketReceiver;
import jpcap.packet.Packet;

public class PacketContents implements PacketReceiver
{
    public void receivePacket(Packet packet)
    {
        Interface.TA_OUTPUT.append(packet.toString() + "\n---------------------------------------------------------------------\n\n");
    }
}