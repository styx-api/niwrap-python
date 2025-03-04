# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_REFINE_SURFACES_METADATA = Metadata(
    id="afa5fdcf50348032d468a3e07292675e06d5374e.boutiques",
    name="mris_refine_surfaces",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisRefineSurfacesParameters = typing.TypedDict('MrisRefineSurfacesParameters', {
    "__STYX_TYPE__": typing.Literal["mris_refine_surfaces"],
    "subject_name": str,
    "hemi": str,
    "hires_volume": str,
    "label_file": str,
    "low_to_hires_xfm": typing.NotRequired[str | None],
    "sdir": typing.NotRequired[str | None],
    "use_mgz": bool,
    "suffix": typing.NotRequired[str | None],
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
        "mris_refine_surfaces": mris_refine_surfaces_cargs,
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
        "mris_refine_surfaces": mris_refine_surfaces_outputs,
    }.get(t)


class MrisRefineSurfacesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_refine_surfaces(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    pial_surface: OutputPathType
    """Refined pial surface for the specified region"""
    white_surface: OutputPathType
    """Refined white matter surface for the specified region"""


def mris_refine_surfaces_params(
    subject_name: str,
    hemi: str,
    hires_volume: str,
    label_file: str,
    low_to_hires_xfm: str | None = None,
    sdir: str | None = None,
    use_mgz: bool = False,
    suffix: str | None = None,
) -> MrisRefineSurfacesParameters:
    """
    Build parameters.
    
    Args:
        subject_name: The name of the subject.
        hemi: The hemisphere to process ('lh' for left hemisphere, 'rh' for\
            right hemisphere).
        hires_volume: The high-resolution volume filename.
        label_file: The label file specifying the region to refine.
        low_to_hires_xfm: The optional low to high resolution transform file.
        sdir: Specify the SUBJECTS_DIR.
        use_mgz: Use .mgz volumes.
        suffix: Add specified suffix to the final surfaces.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_refine_surfaces",
        "subject_name": subject_name,
        "hemi": hemi,
        "hires_volume": hires_volume,
        "label_file": label_file,
        "use_mgz": use_mgz,
    }
    if low_to_hires_xfm is not None:
        params["low_to_hires_xfm"] = low_to_hires_xfm
    if sdir is not None:
        params["sdir"] = sdir
    if suffix is not None:
        params["suffix"] = suffix
    return params


def mris_refine_surfaces_cargs(
    params: MrisRefineSurfacesParameters,
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
    cargs.append("mris_refine_surfaces")
    cargs.append(params.get("subject_name"))
    cargs.append(params.get("hemi"))
    cargs.append(params.get("hires_volume"))
    cargs.append(params.get("label_file"))
    if params.get("low_to_hires_xfm") is not None:
        cargs.append(params.get("low_to_hires_xfm"))
    if params.get("sdir") is not None:
        cargs.extend([
            "-sdir",
            params.get("sdir")
        ])
    if params.get("use_mgz"):
        cargs.append("-mgz")
    if params.get("suffix") is not None:
        cargs.extend([
            "-suffix",
            params.get("suffix")
        ])
    return cargs


def mris_refine_surfaces_outputs(
    params: MrisRefineSurfacesParameters,
    execution: Execution,
) -> MrisRefineSurfacesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisRefineSurfacesOutputs(
        root=execution.output_file("."),
        pial_surface=execution.output_file("$(SUBJECTS_DIR)/" + params.get("subject_name") + "/surf/" + params.get("hemi") + ".pialhires"),
        white_surface=execution.output_file("$(SUBJECTS_DIR)/" + params.get("subject_name") + "/surf/" + params.get("hemi") + ".whitehires"),
    )
    return ret


def mris_refine_surfaces_execute(
    params: MrisRefineSurfacesParameters,
    execution: Execution,
) -> MrisRefineSurfacesOutputs:
    """
    Refines cortical surfaces around the region specified by the label file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisRefineSurfacesOutputs`).
    """
    params = execution.params(params)
    cargs = mris_refine_surfaces_cargs(params, execution)
    ret = mris_refine_surfaces_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_refine_surfaces(
    subject_name: str,
    hemi: str,
    hires_volume: str,
    label_file: str,
    low_to_hires_xfm: str | None = None,
    sdir: str | None = None,
    use_mgz: bool = False,
    suffix: str | None = None,
    runner: Runner | None = None,
) -> MrisRefineSurfacesOutputs:
    """
    Refines cortical surfaces around the region specified by the label file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: The name of the subject.
        hemi: The hemisphere to process ('lh' for left hemisphere, 'rh' for\
            right hemisphere).
        hires_volume: The high-resolution volume filename.
        label_file: The label file specifying the region to refine.
        low_to_hires_xfm: The optional low to high resolution transform file.
        sdir: Specify the SUBJECTS_DIR.
        use_mgz: Use .mgz volumes.
        suffix: Add specified suffix to the final surfaces.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisRefineSurfacesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_REFINE_SURFACES_METADATA)
    params = mris_refine_surfaces_params(
        subject_name=subject_name,
        hemi=hemi,
        hires_volume=hires_volume,
        label_file=label_file,
        low_to_hires_xfm=low_to_hires_xfm,
        sdir=sdir,
        use_mgz=use_mgz,
        suffix=suffix,
    )
    return mris_refine_surfaces_execute(params, execution)


__all__ = [
    "MRIS_REFINE_SURFACES_METADATA",
    "MrisRefineSurfacesOutputs",
    "MrisRefineSurfacesParameters",
    "mris_refine_surfaces",
    "mris_refine_surfaces_params",
]
