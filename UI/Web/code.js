async function capture()
{
    let a = await eel.CheckInterfaceAndCap()();
//    alert(a);
    reader();
}

async function reader()
{
    let report = await eel.reader()();
    alert(report);
}