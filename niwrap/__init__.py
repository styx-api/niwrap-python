"""Neuroimaging python wrappers."""

import importlib
import pkgutil

# Discover niwrap packages
prefix = "niwrap_"
__all__ = {
    name[len(prefix) :]: importlib.import_module(name)
    for _, name, _ in pkgutil.iter_modules()
    if name.startswith(prefix)
}

# Update namespace
globals().update(__all__)

# Clean up namespace
del importlib, pkgutil, prefix
