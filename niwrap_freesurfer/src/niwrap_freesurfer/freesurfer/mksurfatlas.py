# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MKSURFATLAS_METADATA = Metadata(
    id="d79ac3c3008bc4ea34030be87ef82c18eea6b065.boutiques",
    name="mksurfatlas",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MksurfatlasParameters = typing.TypedDict('MksurfatlasParameters', {
    "__STYXTYPE__": typing.Literal["mksurfatlas"],
    "atlas": str,
    "hemi": str,
    "subjects": list[str],
    "surfval": str,
    "surfvaldir": typing.NotRequired[str | None],
    "regsurf": typing.NotRequired[str | None],
    "debug": bool,
    "version": bool,
    "help": bool,
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
        "mksurfatlas": mksurfatlas_cargs,
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
        "mksurfatlas": mksurfatlas_outputs,
    }.get(t)


class MksurfatlasOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mksurfatlas(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_atlas: OutputPathType
    """Resulting atlas file in TIFF format."""


def mksurfatlas_params(
    atlas: str,
    hemi: str,
    subjects: list[str],
    surfval: str,
    surfvaldir: str | None = "label",
    regsurf: str | None = "sphere",
    debug: bool = False,
    version: bool = False,
    help_: bool = False,
) -> MksurfatlasParameters:
    """
    Build parameters.
    
    Args:
        atlas: Save results to this file (tif file).
        hemi: Hemisphere to process.
        subjects: Subject(s) to process. Multiple subjects can be specified by\
            repeating the flag.
        surfval: Surface values file. Looks for\
            subject/surfvaldir/hemi.surfval.
        surfvaldir: Directory for surface values; default is 'label'.
        regsurf: Registration surface; default is 'sphere'.
        debug: Turn on debugging.
        version: Print version and exit.
        help_: Print help and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mksurfatlas",
        "atlas": atlas,
        "hemi": hemi,
        "subjects": subjects,
        "surfval": surfval,
        "debug": debug,
        "version": version,
        "help": help_,
    }
    if surfvaldir is not None:
        params["surfvaldir"] = surfvaldir
    if regsurf is not None:
        params["regsurf"] = regsurf
    return params


def mksurfatlas_cargs(
    params: MksurfatlasParameters,
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
    cargs.append("mksurfatlas")
    cargs.extend([
        "--a",
        params.get("atlas")
    ])
    cargs.extend([
        "--h",
        params.get("hemi")
    ])
    cargs.extend([
        "--s",
        *params.get("subjects")
    ])
    cargs.extend([
        "--v",
        params.get("surfval")
    ])
    if params.get("surfvaldir") is not None:
        cargs.extend([
            "--d",
            params.get("surfvaldir")
        ])
    if params.get("regsurf") is not None:
        cargs.extend([
            "--r",
            params.get("regsurf")
        ])
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("version"):
        cargs.append("--version")
    if params.get("help"):
        cargs.append("--help")
    return cargs


def mksurfatlas_outputs(
    params: MksurfatlasParameters,
    execution: Execution,
) -> MksurfatlasOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MksurfatlasOutputs(
        root=execution.output_file("."),
        output_atlas=execution.output_file(params.get("atlas")),
    )
    return ret


def mksurfatlas_execute(
    params: MksurfatlasParameters,
    execution: Execution,
) -> MksurfatlasOutputs:
    """
    Creates an atlas using mris_make_template. The atlas can then be used to create
    the surface registration for each subject based on this atlas.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MksurfatlasOutputs`).
    """
    params = execution.params(params)
    cargs = mksurfatlas_cargs(params, execution)
    ret = mksurfatlas_outputs(params, execution)
    execution.run(cargs)
    return ret


def mksurfatlas(
    atlas: str,
    hemi: str,
    subjects: list[str],
    surfval: str,
    surfvaldir: str | None = "label",
    regsurf: str | None = "sphere",
    debug: bool = False,
    version: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> MksurfatlasOutputs:
    """
    Creates an atlas using mris_make_template. The atlas can then be used to create
    the surface registration for each subject based on this atlas.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        atlas: Save results to this file (tif file).
        hemi: Hemisphere to process.
        subjects: Subject(s) to process. Multiple subjects can be specified by\
            repeating the flag.
        surfval: Surface values file. Looks for\
            subject/surfvaldir/hemi.surfval.
        surfvaldir: Directory for surface values; default is 'label'.
        regsurf: Registration surface; default is 'sphere'.
        debug: Turn on debugging.
        version: Print version and exit.
        help_: Print help and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MksurfatlasOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MKSURFATLAS_METADATA)
    params = mksurfatlas_params(
        atlas=atlas,
        hemi=hemi,
        subjects=subjects,
        surfval=surfval,
        surfvaldir=surfvaldir,
        regsurf=regsurf,
        debug=debug,
        version=version,
        help_=help_,
    )
    return mksurfatlas_execute(params, execution)


__all__ = [
    "MKSURFATLAS_METADATA",
    "MksurfatlasOutputs",
    "MksurfatlasParameters",
    "mksurfatlas",
    "mksurfatlas_params",
]
