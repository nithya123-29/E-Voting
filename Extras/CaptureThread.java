import javax.swing.SwingUtilities;

public abstract class CaptureThread
{
    //Globals
    private Object value;
    private Thread thread;

    //Nested Class maintains ref to current thread under separate sync control
    private static class ThreadVar
    {
        private Thread thread;
        ThreadVar(Thread t) 
        { 
            thread = t;
        }
        synchronized Thread get()
        {
            return thread;
        }
        synchronized void clear()
        {
            thread = null;
        }
    }

//----------------------------------------------------------
    private ThreadVar threadVar;

    //Accessor Methods
    protected synchronized Object getValue()
    {
        return value;
    }
    private synchronized void setValue(Object x)
    {
        value =x;
    }
//----------------------------------------------------------------

    //Compute values to be returned. Abstract so MUsT be implemented.
    public abstract Object construct();

//----------------------------------------------------------------   
    public void finished();

//----------------------------------------------------------------
    public void interrupt()
    {
        Thread t = threadVar.get();

        if(t != null)
        {
            t.interrupt();
        }
        thread.clear();
    }
//----------------------------------------------------------------
    //Return value created by the constructing Thread, null if
    //constructing or current Thread have been interrupted
    public Object get()
    {
        while(true)
        {
            Thread t = threadVar.get();

            if(t == null)
            {
                return getValue();
            }

            try {
                t.join();
            } catch (InterruptedException e) {
                Thread.currenThread().interrupt(); //propogate
                return null;
            }
        }
    }
//----------------------------------------------------------------
    //Start a thread that will call constructor and exit
    public CaptureThread()
    {
        final Runnable doFinished = new Runnable()
        {
            public void run()
            {
                finished();
            }
        };
        Runnable doConstruct = new Runnable()
        {
            public void run()
            {
                try
                {
                    setValue(construct());
                }
                finally
                {
                    threadVar.clear();
                }

                SwingUtilities.invokeLater(doFinished);
            }
        };

        Thread t = new Thread(doConstruct);
        threadVar = new ThreadVar(t);
    }
//----------------------------------------------------------------
    public void start()
    {
        Thread t = threadVar.get();

        if(t != null)
        {
            t.start();
        }
    }
//----------------------------------------------------------------

}