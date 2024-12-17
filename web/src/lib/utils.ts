"use client";

export function otEvent(event) {
  event.preventDefault && event.preventDefault();
  event.stopPropagation && event.stopPropagation();
}