declare global {
  export interface Alert {
    message: string;
    type: "info" | "success" | "error" | "warning";
  }
}
