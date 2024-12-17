"use client";

//import type {RootLayoutProps} from "next"
//import { Inter as FontSans } from "next/font/google";
import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';

import "./globals.css";
import CssBaseline from "@mui/material/CssBaseline";
import Paper from "@mui/material/Paper";
import { UIContextProvider } from "@/lib/ui.context";
import ErrorBoundary from "@/components/error";

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {

  return (
    <html lang="en" suppressHydrationWarning>
      <head>
        <meta name="viewport" content="initial-scale=1, width=device-width" />
      </head>
      <body style={{ background: "white" }} >
        <ErrorBoundary>
          <UIContextProvider>
            <CssBaseline />
            {children}
          </UIContextProvider>
        </ErrorBoundary>
      </body>
    </html>
  );
}
