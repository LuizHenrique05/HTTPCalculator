using System;
using System.IO;
using System.Net;

namespace calculadoraClient
{
    class Program
    {
        static void Main(string[] args)
        {
            // Create a request for the URL.
            WebRequest request = WebRequest.Create(
            //**host**/add/?a=1&b=1     ADD
            //**host**/mult/?a=1&b=1    MULT
                "http://127.0.0.1:8000/mult/?a=1&b=1"); 
            // If required by the server, set the credentials.
            request.Credentials = CredentialCache.DefaultCredentials;

            // Get the response.
            WebResponse response = request.GetResponse();
            // Display the status.
            Console.WriteLine(((HttpWebResponse)response).StatusDescription);

            // Get the stream containing content returned by the server.
            // The using block ensures the stream is automatically closed.
            using (Stream dataStream = response.GetResponseStream())
            {
                // Open the stream using a StreamReader for easy access.
                StreamReader reader = new StreamReader(dataStream);
                // Read the content.
                string responseFromServer = reader.ReadToEnd();
                // Display the content.
                Console.WriteLine(responseFromServer);
            }

            // Close the response.
            response.Close();
        }
    }
}
