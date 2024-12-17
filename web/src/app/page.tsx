"use client";
import { useState } from "react";
import { TextField, Button, Container, Typography, Box } from "@mui/material";
import { submitQuestion } from "../api"
import { useUIContext } from "@/lib";

export default function Home() {
  const [question, setQuestion] = useState("What player at the Bears expected to draft first in the 2024 NFL draft?");
  const [answer, setAnswer] = useState("");
  const ui = useUIContext();

  const handleSubmit = async () => {
    const resp = await submitQuestion(ui, { question });
    setAnswer(resp.answer);
  };

  return (
    <Container maxWidth="sm" style={{ marginTop: "50px" }}>
      <Box textAlign="center" mb={3}>
        <Typography variant="subtitle1">
          Ask a Question
        </Typography>
      </Box>

      <TextField
        fullWidth
        label="Your Question"
        variant="outlined"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        margin="normal"
      />

      <Box textAlign="center" mt={2}>
        <Button
          variant="contained"
          color="primary"
          onClick={handleSubmit}
          disabled={!question.trim()}
        >
          Submit
        </Button>
      </Box>

      {answer && (
        <Box mt={4} p={2} border={1} borderRadius={2} borderColor="grey.300">
          <Typography variant="h6">Response:</Typography>
          <Typography>{answer}</Typography>
        </Box>
      )}
    </Container>
  );
}
