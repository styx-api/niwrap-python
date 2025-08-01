# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

NEURO_DECONVOLVE_PY_METADATA = Metadata(
    id="154583959fdfd006d275bd6d8f9c6a8e067b7747.boutiques",
    name="neuro_deconvolve.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


NeuroDeconvolvePyParameters = typing.TypedDict('NeuroDeconvolvePyParameters', {
    "__STYXTYPE__": typing.Literal["neuro_deconvolve.py"],
    "input_file": InputPathType,
    "prefix": str,
    "script": str,
    "kernel": typing.NotRequired[str | None],
    "kernel_file": typing.NotRequired[str | None],
    "mask_dset": typing.NotRequired[InputPathType | None],
    "old_style": bool,
    "tr": typing.NotRequired[float | None],
    "tr_nup": typing.NotRequired[float | None],
    "verbosity": typing.NotRequired[float | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "neuro_deconvolve.py": neuro_deconvolve_py_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "neuro_deconvolve.py": neuro_deconvolve_py_outputs,
    }.get(t)


class NeuroDeconvolvePyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `neuro_deconvolve_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_head: OutputPathType
    """Main default output head file"""
    output_brik: OutputPathType
    """Main default output BRIK file"""
    kernel_file_out: OutputPathType | None
    """File storing the response kernel"""


def neuro_deconvolve_py_params(
    input_file: InputPathType,
    prefix: str,
    script: str,
    kernel: str | None = None,
    kernel_file: str | None = None,
    mask_dset: InputPathType | None = None,
    old_style: bool = False,
    tr: float | None = None,
    tr_nup: float | None = None,
    verbosity: float | None = None,
) -> NeuroDeconvolvePyParameters:
    """
    Build parameters.
    
    Args:
        input_file: Set the data to deconvolve.
        prefix: Set the prefix for output filenames.
        script: Specify the name of the output script.
        kernel: Set the response kernel.
        kernel_file: Set the filename to store the kernel in; should be at the\
            upsampled TR.
        mask_dset: Set a mask dataset for 3dTfitter to use.
        old_style: Make old-style script (pre-2015.02.24) for 1D case.
        tr: Set the scanner TR; needed for 1D formatted input files.
        tr_nup: Upsample factor for TR; number of pieces each original TR is\
            divided into.
        verbosity: Set the verbose level.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "neuro_deconvolve.py",
        "input_file": input_file,
        "prefix": prefix,
        "script": script,
        "old_style": old_style,
    }
    if kernel is not None:
        params["kernel"] = kernel
    if kernel_file is not None:
        params["kernel_file"] = kernel_file
    if mask_dset is not None:
        params["mask_dset"] = mask_dset
    if tr is not None:
        params["tr"] = tr
    if tr_nup is not None:
        params["tr_nup"] = tr_nup
    if verbosity is not None:
        params["verbosity"] = verbosity
    return params


def neuro_deconvolve_py_cargs(
    params: NeuroDeconvolvePyParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("neuro_deconvolve.py")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(params.get("prefix"))
    cargs.append(params.get("script"))
    if params.get("kernel") is not None:
        cargs.extend([
            "-kernel",
            params.get("kernel")
        ])
    if params.get("kernel_file") is not None:
        cargs.extend([
            "-kernel_file",
            params.get("kernel_file")
        ])
    if params.get("mask_dset") is not None:
        cargs.extend([
            "-mask_dset",
            execution.input_file(params.get("mask_dset"))
        ])
    if params.get("old_style"):
        cargs.append("-old")
    if params.get("tr") is not None:
        cargs.extend([
            "-tr",
            str(params.get("tr"))
        ])
    if params.get("tr_nup") is not None:
        cargs.extend([
            "-tr_nup",
            str(params.get("tr_nup"))
        ])
    if params.get("verbosity") is not None:
        cargs.extend([
            "-verb",
            str(params.get("verbosity"))
        ])
    return cargs


def neuro_deconvolve_py_outputs(
    params: NeuroDeconvolvePyParameters,
    execution: Execution,
) -> NeuroDeconvolvePyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = NeuroDeconvolvePyOutputs(
        root=execution.output_file("."),
        output_head=execution.output_file(params.get("prefix") + "+orig.HEAD"),
        output_brik=execution.output_file(params.get("prefix") + "+orig.BRIK"),
        kernel_file_out=execution.output_file(params.get("kernel_file")) if (params.get("kernel_file") is not None) else None,
    )
    return ret


def neuro_deconvolve_py_execute(
    params: NeuroDeconvolvePyParameters,
    execution: Execution,
) -> NeuroDeconvolvePyOutputs:
    """
    Generate a script to apply 3dTfitter to deconvolve an MRI signal (BOLD response
    curve) into a neuro response curve.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `NeuroDeconvolvePyOutputs`).
    """
    params = execution.params(params)
    cargs = neuro_deconvolve_py_cargs(params, execution)
    ret = neuro_deconvolve_py_outputs(params, execution)
    execution.run(cargs)
    return ret


def neuro_deconvolve_py(
    input_file: InputPathType,
    prefix: str,
    script: str,
    kernel: str | None = None,
    kernel_file: str | None = None,
    mask_dset: InputPathType | None = None,
    old_style: bool = False,
    tr: float | None = None,
    tr_nup: float | None = None,
    verbosity: float | None = None,
    runner: Runner | None = None,
) -> NeuroDeconvolvePyOutputs:
    """
    Generate a script to apply 3dTfitter to deconvolve an MRI signal (BOLD response
    curve) into a neuro response curve.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Set the data to deconvolve.
        prefix: Set the prefix for output filenames.
        script: Specify the name of the output script.
        kernel: Set the response kernel.
        kernel_file: Set the filename to store the kernel in; should be at the\
            upsampled TR.
        mask_dset: Set a mask dataset for 3dTfitter to use.
        old_style: Make old-style script (pre-2015.02.24) for 1D case.
        tr: Set the scanner TR; needed for 1D formatted input files.
        tr_nup: Upsample factor for TR; number of pieces each original TR is\
            divided into.
        verbosity: Set the verbose level.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `NeuroDeconvolvePyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(NEURO_DECONVOLVE_PY_METADATA)
    params = neuro_deconvolve_py_params(
        input_file=input_file,
        prefix=prefix,
        script=script,
        kernel=kernel,
        kernel_file=kernel_file,
        mask_dset=mask_dset,
        old_style=old_style,
        tr=tr,
        tr_nup=tr_nup,
        verbosity=verbosity,
    )
    return neuro_deconvolve_py_execute(params, execution)


__all__ = [
    "NEURO_DECONVOLVE_PY_METADATA",
    "NeuroDeconvolvePyOutputs",
    "NeuroDeconvolvePyParameters",
    "neuro_deconvolve_py",
    "neuro_deconvolve_py_params",
]
