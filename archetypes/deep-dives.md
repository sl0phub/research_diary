+++
title = "Exploration — {{ replace .Name "-" " " | title }}"
date = {{ now.UTC.Format "2006-01-02T15:04:05Z" }}
type = "deep-dives"
tags = ["exploration"]
slug = "{{ .Name }}"
summary = ""
+++

{{/* The title prefix and the first tag are the mode: "Exploration — " with
     `exploration`, or "Breakdown — " with `breakdown`. Exactly one of the two.
     See AGENTS.md §5. */}}

## Background

## Current State

## Future Outlook

## References
