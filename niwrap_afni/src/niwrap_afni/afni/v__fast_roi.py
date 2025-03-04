# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__FAST_ROI_METADATA = Metadata(
    id="3e8aa0aa33715b8e34aca3647b6dda45cf739777.boutiques",
    name="@fast_roi",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VFastRoiParameters = typing.TypedDict('VFastRoiParameters', {
    "__STYX_TYPE__": typing.Literal["@fast_roi"],
    "region": list[str],
    "drawn_roi": typing.NotRequired[InputPathType | None],
    "anat": InputPathType,
    "anat_ns": typing.NotRequired[InputPathType | None],
    "base": InputPathType,
    "roi_grid": InputPathType,
    "prefix": str,
    "time": bool,
    "twopass": bool,
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
        "@fast_roi": v__fast_roi_cargs,
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
        "@fast_roi": v__fast_roi_outputs,
    }.get(t)


class VFastRoiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__fast_roi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    roi_output: OutputPathType
    """ROI output volume with the specified prefix."""


def v__fast_roi_params(
    region: list[str],
    anat: InputPathType,
    base: InputPathType,
    roi_grid: InputPathType,
    prefix: str,
    drawn_roi: InputPathType | None = None,
    anat_ns: InputPathType | None = None,
    time_: bool = False,
    twopass: bool = False,
    help_: bool = False,
) -> VFastRoiParameters:
    """
    Build parameters.
    
    Args:
        region: Symbolic atlas-based region name. Use repeated instances to\
            specify a mask of numerous regions. Each region is assigned a power of\
            2 integer in the output mask.
        anat: ANAT is the volume to be put in standard space. If ANAT is\
            already in TLRC space, there is no need for -base option.
        base: Name of the reference TLRC volume.
        roi_grid: The volume that defines the final ROI's grid.
        prefix: Prefix used to tag the names the ROIs output.
        drawn_roi: A user drawn ROI in standard (tlrc) space. This ROI gets\
            added with the REGION ROI.
        anat_ns: Same as -anat, but indicates that the skull has been removed\
            already.
        time_: Output elapsed time reports.
        twopass: Make TLRC transformation more robust. Use it if TLRC transform\
            step fails.
        help_: Output help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@fast_roi",
        "region": region,
        "anat": anat,
        "base": base,
        "roi_grid": roi_grid,
        "prefix": prefix,
        "time": time_,
        "twopass": twopass,
        "help": help_,
    }
    if drawn_roi is not None:
        params["drawn_roi"] = drawn_roi
    if anat_ns is not None:
        params["anat_ns"] = anat_ns
    return params


def v__fast_roi_cargs(
    params: VFastRoiParameters,
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
    cargs.append("@fast_roi")
    cargs.extend([
        "-region",
        *params.get("region")
    ])
    if params.get("drawn_roi") is not None:
        cargs.extend([
            "-drawn_roi",
            execution.input_file(params.get("drawn_roi"))
        ])
    cargs.extend([
        "-anat",
        execution.input_file(params.get("anat"))
    ])
    if params.get("anat_ns") is not None:
        cargs.extend([
            "-anat_ns",
            execution.input_file(params.get("anat_ns"))
        ])
    cargs.extend([
        "-base",
        execution.input_file(params.get("base"))
    ])
    cargs.extend([
        "-roi_grid",
        execution.input_file(params.get("roi_grid"))
    ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("time"):
        cargs.append("--time")
    if params.get("twopass"):
        cargs.append("--twopass")
    if params.get("help"):
        cargs.append("--help")
    return cargs


def v__fast_roi_outputs(
    params: VFastRoiParameters,
    execution: Execution,
) -> VFastRoiOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VFastRoiOutputs(
        root=execution.output_file("."),
        roi_output=execution.output_file("ROI." + params.get("prefix") + "+orig"),
    )
    return ret


def v__fast_roi_execute(
    params: VFastRoiParameters,
    execution: Execution,
) -> VFastRoiOutputs:
    """
    Creates Atlas-based ROI masked in ANAT's original space. The script executes
    rapidly for realtime fMRI applications.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VFastRoiOutputs`).
    """
    params = execution.params(params)
    cargs = v__fast_roi_cargs(params, execution)
    ret = v__fast_roi_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__fast_roi(
    region: list[str],
    anat: InputPathType,
    base: InputPathType,
    roi_grid: InputPathType,
    prefix: str,
    drawn_roi: InputPathType | None = None,
    anat_ns: InputPathType | None = None,
    time_: bool = False,
    twopass: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> VFastRoiOutputs:
    """
    Creates Atlas-based ROI masked in ANAT's original space. The script executes
    rapidly for realtime fMRI applications.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        region: Symbolic atlas-based region name. Use repeated instances to\
            specify a mask of numerous regions. Each region is assigned a power of\
            2 integer in the output mask.
        anat: ANAT is the volume to be put in standard space. If ANAT is\
            already in TLRC space, there is no need for -base option.
        base: Name of the reference TLRC volume.
        roi_grid: The volume that defines the final ROI's grid.
        prefix: Prefix used to tag the names the ROIs output.
        drawn_roi: A user drawn ROI in standard (tlrc) space. This ROI gets\
            added with the REGION ROI.
        anat_ns: Same as -anat, but indicates that the skull has been removed\
            already.
        time_: Output elapsed time reports.
        twopass: Make TLRC transformation more robust. Use it if TLRC transform\
            step fails.
        help_: Output help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VFastRoiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__FAST_ROI_METADATA)
    params = v__fast_roi_params(
        region=region,
        drawn_roi=drawn_roi,
        anat=anat,
        anat_ns=anat_ns,
        base=base,
        roi_grid=roi_grid,
        prefix=prefix,
        time_=time_,
        twopass=twopass,
        help_=help_,
    )
    return v__fast_roi_execute(params, execution)


__all__ = [
    "VFastRoiOutputs",
    "VFastRoiParameters",
    "V__FAST_ROI_METADATA",
    "v__fast_roi",
    "v__fast_roi_params",
]
