async function capture()
{
    var decision = prompt("Do you want to sniff the network: Y / N");
    if(decision == 'y' || decision == 'Y') {;}
    console.log("Hi");
//    else if(decision == 'n' || decision == 'N') close();
//    else alert('Unsupported Input');
    await eel.sniff()();
}

function close()
{
    alert('Bye!!');
    system.exit();
}