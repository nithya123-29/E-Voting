async function capture()
{
    await eel.CheckInterfaceAndCap()();
}

async function reader()
{
    report = await eel.Reading()();
    document.getElementById('details').innerHTML = report;
}

async function graph()
{
    report = await eel.Graph()();
    document.getElementById('details').innerHTML = report;
    $(function(){
      $("#includeSrcGraph").load("srcIPOccurance.html");
    });
    $(function(){
      $("#includefrequencyProtocol").load("frequencyProtocol.html");
    });
    $(function(){
      $("#includeIoGraph").load("iograph.html");
    });

}