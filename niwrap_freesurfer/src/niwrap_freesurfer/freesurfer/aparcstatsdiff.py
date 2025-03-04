# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

APARCSTATSDIFF_METADATA = Metadata(
    id="c9cea4353f4e4aca9c0c94b627fe528484a4d224.boutiques",
    name="aparcstatsdiff",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


AparcstatsdiffParameters = typing.TypedDict('AparcstatsdiffParameters', {
    "__STYX_TYPE__": typing.Literal["aparcstatsdiff"],
    "subj1": str,
    "subj2": str,
    "hemi": str,
    "parc": str,
    "meas": str,
    "outdir": typing.NotRequired[str | None],
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
        "aparcstatsdiff": aparcstatsdiff_cargs,
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
        "aparcstatsdiff": aparcstatsdiff_outputs,
    }.get(t)


class AparcstatsdiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `aparcstatsdiff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output table with percentage differences"""


def aparcstatsdiff_params(
    subj1: str,
    subj2: str,
    hemi: str,
    parc: str,
    meas: str,
    outdir: str | None = None,
) -> AparcstatsdiffParameters:
    """
    Build parameters.
    
    Args:
        subj1: Subject 1 identifier.
        subj2: Subject 2 identifier.
        hemi: Hemisphere (rh or lh).
        parc: Parcellation scheme (aparc or aparc.a2009s).
        meas: Measure type (area, volume, or thickness).
        outdir: Directory to write the output table file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "aparcstatsdiff",
        "subj1": subj1,
        "subj2": subj2,
        "hemi": hemi,
        "parc": parc,
        "meas": meas,
    }
    if outdir is not None:
        params["outdir"] = outdir
    return params


def aparcstatsdiff_cargs(
    params: AparcstatsdiffParameters,
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
    cargs.append("aparcstatsdiff")
    cargs.append(params.get("subj1"))
    cargs.append(params.get("subj2"))
    cargs.append(params.get("hemi"))
    cargs.append(params.get("parc"))
    cargs.append(params.get("meas"))
    if params.get("outdir") is not None:
        cargs.append(params.get("outdir"))
    return cargs


def aparcstatsdiff_outputs(
    params: AparcstatsdiffParameters,
    execution: Execution,
) -> AparcstatsdiffOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AparcstatsdiffOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("aparcstats-" + params.get("hemi") + "." + params.get("parc") + "." + params.get("meas") + ".txt"),
    )
    return ret


def aparcstatsdiff_execute(
    params: AparcstatsdiffParameters,
    execution: Execution,
) -> AparcstatsdiffOutputs:
    """
    Utility to calculate percentage differences in aparc morphometry data between
    two subjects.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AparcstatsdiffOutputs`).
    """
    params = execution.params(params)
    cargs = aparcstatsdiff_cargs(params, execution)
    ret = aparcstatsdiff_outputs(params, execution)
    execution.run(cargs)
    return ret


def aparcstatsdiff(
    subj1: str,
    subj2: str,
    hemi: str,
    parc: str,
    meas: str,
    outdir: str | None = None,
    runner: Runner | None = None,
) -> AparcstatsdiffOutputs:
    """
    Utility to calculate percentage differences in aparc morphometry data between
    two subjects.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subj1: Subject 1 identifier.
        subj2: Subject 2 identifier.
        hemi: Hemisphere (rh or lh).
        parc: Parcellation scheme (aparc or aparc.a2009s).
        meas: Measure type (area, volume, or thickness).
        outdir: Directory to write the output table file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AparcstatsdiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(APARCSTATSDIFF_METADATA)
    params = aparcstatsdiff_params(
        subj1=subj1,
        subj2=subj2,
        hemi=hemi,
        parc=parc,
        meas=meas,
        outdir=outdir,
    )
    return aparcstatsdiff_execute(params, execution)


__all__ = [
    "APARCSTATSDIFF_METADATA",
    "AparcstatsdiffOutputs",
    "AparcstatsdiffParameters",
    "aparcstatsdiff",
    "aparcstatsdiff_params",
]
