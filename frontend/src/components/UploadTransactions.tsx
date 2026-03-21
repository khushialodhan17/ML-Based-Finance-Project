import { useState } from "react";

export default function UploadTransactions() {
  const [file, setFile] = useState<File | null>(null);
 type Transaction = {
  date: string;
  description: string;
  amount: number;
  type: string;
};

const [data, setData] = useState<{
  count: number;
  transactions: Transaction[];
} | null>(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file first");
      return;
    }

    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      // api key
      const res = await fetch("http://127.0.0.1:8000/upload-transactions", {
        method: "POST",
        body: formData,
      });

      const result = await res.json();
      setData(result);
    } catch (error) {
      console.error("Error uploading file:", error);
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Upload Bank Statement</h2>

      {/* File Input */}
      <input
        type="file"
        accept=".csv , .pdf"
        onChange={(e) => setFile(e.target.files?.[0] || null)}
      />

      <br /><br />

      {/* Upload Button */}
      <button onClick={handleUpload}>
        {loading ? "Uploading..." : "Upload"}
      </button>

      <br /><br />

      {/* Response Display */}
      {data && (
        <div>
          <h3>Total Transactions: {data.count}</h3>

          <pre style={{ textAlign: "left" }}>
            {JSON.stringify(data.transactions, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}