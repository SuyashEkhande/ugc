import type { components, operations } from "./openapi";

export const contractsVersion = "0.1.0";

export type { components, operations };
export type HealthResponse = components["schemas"]["HealthResponse"];
export type ProjectStatus = components["schemas"]["ProjectStatus"];
export type ProjectSummary = components["schemas"]["ProjectSummary"];
export type ProjectListResponse = components["schemas"]["ProjectListResponse"];
