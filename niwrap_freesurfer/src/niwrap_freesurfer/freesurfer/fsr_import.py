# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSR_IMPORT_METADATA = Metadata(
    id="b30a1cfc4e13a11d981b6cbab57fcadbba24f4a3.boutiques",
    name="fsr-import",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


FsrImportParameters = typing.TypedDict('FsrImportParameters', {
    "__STYX_TYPE__": typing.Literal["fsr-import"],
    "outdir": str,
    "t1w_input": typing.NotRequired[list[InputPathType] | None],
    "t2w_input": typing.NotRequired[list[InputPathType] | None],
    "flair_input": typing.NotRequired[list[InputPathType] | None],
    "custom_mode_input": typing.NotRequired[list[str] | None],
    "force_update": bool,
    "no_conform": bool,
    "hires": bool,
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
        "fsr-import": fsr_import_cargs,
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
        "fsr-import": fsr_import_outputs,
    }.get(t)


class FsrImportOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsr_import(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_t1w: OutputPathType
    """Output directory for T1-weighted images"""
    out_t2w: OutputPathType
    """Output directory for T2-weighted images"""
    out_flair: OutputPathType
    """Output directory for FLAIR images"""
    out_custom_modes: OutputPathType
    """Output directory for custom modality images based on mode"""


def fsr_import_params(
    outdir: str,
    t1w_input: list[InputPathType] | None = None,
    t2w_input: list[InputPathType] | None = None,
    flair_input: list[InputPathType] | None = None,
    custom_mode_input: list[str] | None = None,
    force_update: bool = False,
    no_conform: bool = False,
    hires: bool = False,
) -> FsrImportParameters:
    """
    Build parameters.
    
    Args:
        outdir: Root directory for output data.
        t1w_input: Input T1-weighted image files.
        t2w_input: Input T2-weighted image files.
        flair_input: Input FLAIR image files.
        custom_mode_input: Custom modality image file with specified mode name\
            (not t1w, t2w, or flair).
        force_update: Update files regardless of timestamp.
        no_conform: Do not conform inputs to 1mm, 256 dimensions.
        hires: Same as --no-conform.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsr-import",
        "outdir": outdir,
        "force_update": force_update,
        "no_conform": no_conform,
        "hires": hires,
    }
    if t1w_input is not None:
        params["t1w_input"] = t1w_input
    if t2w_input is not None:
        params["t2w_input"] = t2w_input
    if flair_input is not None:
        params["flair_input"] = flair_input
    if custom_mode_input is not None:
        params["custom_mode_input"] = custom_mode_input
    return params


def fsr_import_cargs(
    params: FsrImportParameters,
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
    cargs.append("fsr-import")
    cargs.extend([
        "--o",
        params.get("outdir")
    ])
    if params.get("t1w_input") is not None:
        cargs.extend([
            "--t1w",
            *[execution.input_file(f) for f in params.get("t1w_input")]
        ])
    if params.get("t2w_input") is not None:
        cargs.extend([
            "--t2w",
            *[execution.input_file(f) for f in params.get("t2w_input")]
        ])
    if params.get("flair_input") is not None:
        cargs.extend([
            "--flair",
            *[execution.input_file(f) for f in params.get("flair_input")]
        ])
    if params.get("custom_mode_input") is not None:
        cargs.extend([
            "--mode",
            *params.get("custom_mode_input")
        ])
    if params.get("force_update"):
        cargs.append("--force-update")
    if params.get("no_conform"):
        cargs.append("--no-conform")
    if params.get("hires"):
        cargs.append("--hires")
    return cargs


def fsr_import_outputs(
    params: FsrImportParameters,
    execution: Execution,
) -> FsrImportOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FsrImportOutputs(
        root=execution.output_file("."),
        out_t1w=execution.output_file(params.get("outdir") + "/t1w/*.mgz"),
        out_t2w=execution.output_file(params.get("outdir") + "/t2w/*.mgz"),
        out_flair=execution.output_file(params.get("outdir") + "/flair/*.mgz"),
        out_custom_modes=execution.output_file(params.get("outdir") + "/*/*.mgz"),
    )
    return ret


def fsr_import_execute(
    params: FsrImportParameters,
    execution: Execution,
) -> FsrImportOutputs:
    """
    Copies/converts data into a directory structure for samseg-expected format.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FsrImportOutputs`).
    """
    params = execution.params(params)
    cargs = fsr_import_cargs(params, execution)
    ret = fsr_import_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsr_import(
    outdir: str,
    t1w_input: list[InputPathType] | None = None,
    t2w_input: list[InputPathType] | None = None,
    flair_input: list[InputPathType] | None = None,
    custom_mode_input: list[str] | None = None,
    force_update: bool = False,
    no_conform: bool = False,
    hires: bool = False,
    runner: Runner | None = None,
) -> FsrImportOutputs:
    """
    Copies/converts data into a directory structure for samseg-expected format.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        outdir: Root directory for output data.
        t1w_input: Input T1-weighted image files.
        t2w_input: Input T2-weighted image files.
        flair_input: Input FLAIR image files.
        custom_mode_input: Custom modality image file with specified mode name\
            (not t1w, t2w, or flair).
        force_update: Update files regardless of timestamp.
        no_conform: Do not conform inputs to 1mm, 256 dimensions.
        hires: Same as --no-conform.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FsrImportOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSR_IMPORT_METADATA)
    params = fsr_import_params(
        outdir=outdir,
        t1w_input=t1w_input,
        t2w_input=t2w_input,
        flair_input=flair_input,
        custom_mode_input=custom_mode_input,
        force_update=force_update,
        no_conform=no_conform,
        hires=hires,
    )
    return fsr_import_execute(params, execution)


__all__ = [
    "FSR_IMPORT_METADATA",
    "FsrImportOutputs",
    "FsrImportParameters",
    "fsr_import",
    "fsr_import_params",
]
