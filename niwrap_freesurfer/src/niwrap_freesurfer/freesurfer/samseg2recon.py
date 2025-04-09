# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SAMSEG2RECON_METADATA = Metadata(
    id="97f76cfe683f565bad32807ad5fd88ea96f398c8.boutiques",
    name="samseg2recon",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


Samseg2reconParameters = typing.TypedDict('Samseg2reconParameters', {
    "__STYX_TYPE__": typing.Literal["samseg2recon"],
    "subject": str,
    "samseg_dir": typing.NotRequired[str | None],
    "no_cc": bool,
    "fill": bool,
    "normalization2": bool,
    "uchar": bool,
    "no_keep_exc": bool,
    "long_tp": typing.NotRequired[float | None],
    "base": bool,
    "mask_file": typing.NotRequired[InputPathType | None],
    "from_recon_all": bool,
    "force_update": bool,
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
        "samseg2recon": samseg2recon_cargs,
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
        "samseg2recon": samseg2recon_outputs,
    }.get(t)


class Samseg2reconOutputs(typing.NamedTuple):
    """
    Output object returned when calling `samseg2recon(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    filled_mgz: OutputPathType
    """Filled MRI volume for the subject, if --fill is used."""
    norm_mgz: OutputPathType
    """Normalized MRI volume created from brain.mgz if --normalization2 is
    used."""
    orig_mgz: OutputPathType
    """Original MRI conformed volume."""


def samseg2recon_params(
    subject: str,
    samseg_dir: str | None = None,
    no_cc: bool = False,
    fill: bool = False,
    normalization2: bool = False,
    uchar: bool = False,
    no_keep_exc: bool = False,
    long_tp: float | None = None,
    base: bool = False,
    mask_file: InputPathType | None = None,
    from_recon_all: bool = False,
    force_update: bool = False,
) -> Samseg2reconParameters:
    """
    Build parameters.
    
    Args:
        subject: Subject identifier.
        samseg_dir: Output directory from samseg or samseg-long. Defaults to\
            subject/mri/samseg if not supplied.
        no_cc: Do not do corpus callosum segmentation.
        fill: Use samseg to create the filled.mgz used for tessellation.
        normalization2: Seg brain.mgz to norm.mgz.
        uchar: Convert to uchar.
        no_keep_exc: Do not keep extracerebral segmentations.
        long_tp: Process specific time point (TP) number from samsegdir.
        base: Process base, will find folder called base in samsegdir.
        mask_file: Use provided mask as brainmask instead of computing from seg.
        from_recon_all: Indicates execution from recon-all, preventing\
            overwrite of rawavg.mgz and orig.mgz.
        force_update: Force update of the subject directory.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "samseg2recon",
        "subject": subject,
        "no_cc": no_cc,
        "fill": fill,
        "normalization2": normalization2,
        "uchar": uchar,
        "no_keep_exc": no_keep_exc,
        "base": base,
        "from_recon_all": from_recon_all,
        "force_update": force_update,
    }
    if samseg_dir is not None:
        params["samseg_dir"] = samseg_dir
    if long_tp is not None:
        params["long_tp"] = long_tp
    if mask_file is not None:
        params["mask_file"] = mask_file
    return params


def samseg2recon_cargs(
    params: Samseg2reconParameters,
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
    cargs.append("samseg2recon")
    cargs.extend([
        "--s",
        params.get("subject")
    ])
    if params.get("samseg_dir") is not None:
        cargs.extend([
            "--samseg",
            params.get("samseg_dir")
        ])
    if params.get("no_cc"):
        cargs.append("--no-cc")
    if params.get("fill"):
        cargs.append("--fill")
    if params.get("normalization2"):
        cargs.append("--normalization2")
    if params.get("uchar"):
        cargs.append("--uchar")
    if params.get("no_keep_exc"):
        cargs.append("--no-keep-exc")
    if params.get("long_tp") is not None:
        cargs.extend([
            "--long",
            str(params.get("long_tp"))
        ])
    if params.get("base"):
        cargs.append("--base")
    if params.get("mask_file") is not None:
        cargs.extend([
            "--m",
            execution.input_file(params.get("mask_file"))
        ])
    if params.get("from_recon_all"):
        cargs.append("--from-recon-all")
    if params.get("force_update"):
        cargs.append("--force-update")
    return cargs


def samseg2recon_outputs(
    params: Samseg2reconParameters,
    execution: Execution,
) -> Samseg2reconOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Samseg2reconOutputs(
        root=execution.output_file("."),
        filled_mgz=execution.output_file(params.get("subject") + "/mri/filled.mgz"),
        norm_mgz=execution.output_file(params.get("subject") + "/mri/norm.mgz"),
        orig_mgz=execution.output_file(params.get("subject") + "/mri/orig/001.mgz"),
    )
    return ret


def samseg2recon_execute(
    params: Samseg2reconParameters,
    execution: Execution,
) -> Samseg2reconOutputs:
    """
    Creates and populates a subjects directory for use with recon-all from SAMSEG
    outputs.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Samseg2reconOutputs`).
    """
    params = execution.params(params)
    cargs = samseg2recon_cargs(params, execution)
    ret = samseg2recon_outputs(params, execution)
    execution.run(cargs)
    return ret


def samseg2recon(
    subject: str,
    samseg_dir: str | None = None,
    no_cc: bool = False,
    fill: bool = False,
    normalization2: bool = False,
    uchar: bool = False,
    no_keep_exc: bool = False,
    long_tp: float | None = None,
    base: bool = False,
    mask_file: InputPathType | None = None,
    from_recon_all: bool = False,
    force_update: bool = False,
    runner: Runner | None = None,
) -> Samseg2reconOutputs:
    """
    Creates and populates a subjects directory for use with recon-all from SAMSEG
    outputs.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject identifier.
        samseg_dir: Output directory from samseg or samseg-long. Defaults to\
            subject/mri/samseg if not supplied.
        no_cc: Do not do corpus callosum segmentation.
        fill: Use samseg to create the filled.mgz used for tessellation.
        normalization2: Seg brain.mgz to norm.mgz.
        uchar: Convert to uchar.
        no_keep_exc: Do not keep extracerebral segmentations.
        long_tp: Process specific time point (TP) number from samsegdir.
        base: Process base, will find folder called base in samsegdir.
        mask_file: Use provided mask as brainmask instead of computing from seg.
        from_recon_all: Indicates execution from recon-all, preventing\
            overwrite of rawavg.mgz and orig.mgz.
        force_update: Force update of the subject directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Samseg2reconOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SAMSEG2RECON_METADATA)
    params = samseg2recon_params(
        subject=subject,
        samseg_dir=samseg_dir,
        no_cc=no_cc,
        fill=fill,
        normalization2=normalization2,
        uchar=uchar,
        no_keep_exc=no_keep_exc,
        long_tp=long_tp,
        base=base,
        mask_file=mask_file,
        from_recon_all=from_recon_all,
        force_update=force_update,
    )
    return samseg2recon_execute(params, execution)


__all__ = [
    "SAMSEG2RECON_METADATA",
    "Samseg2reconOutputs",
    "Samseg2reconParameters",
    "samseg2recon",
    "samseg2recon_params",
]
