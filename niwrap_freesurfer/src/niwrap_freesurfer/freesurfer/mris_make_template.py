# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_MAKE_TEMPLATE_METADATA = Metadata(
    id="f241b82eadd84acf1f6370c052eca75a53412d4e.boutiques",
    name="mris_make_template",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisMakeTemplateParameters = typing.TypedDict('MrisMakeTemplateParameters', {
    "__STYXTYPE__": typing.Literal["mris_make_template"],
    "hemi": str,
    "surface_name": str,
    "subjects": list[str],
    "output_name": str,
    "addframe_parameters": typing.NotRequired[list[str] | None],
    "vector": bool,
    "norot": bool,
    "rot": bool,
    "annot": bool,
    "overlay_parameters": typing.NotRequired[list[str] | None],
    "overlay_dir": typing.NotRequired[str | None],
    "scale": typing.NotRequired[float | None],
    "surf_dir": typing.NotRequired[str | None],
    "smooth_iterations": typing.NotRequired[float | None],
    "subjects_dir": typing.NotRequired[str | None],
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
        "mris_make_template": mris_make_template_cargs,
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
    }.get(t)


class MrisMakeTemplateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_make_template(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_make_template_params(
    hemi: str,
    surface_name: str,
    subjects: list[str],
    output_name: str,
    addframe_parameters: list[str] | None = None,
    vector: bool = False,
    norot: bool = False,
    rot: bool = False,
    annot: bool = False,
    overlay_parameters: list[str] | None = None,
    overlay_dir: str | None = None,
    scale: float | None = None,
    surf_dir: str | None = None,
    smooth_iterations: float | None = None,
    subjects_dir: str | None = None,
) -> MrisMakeTemplateParameters:
    """
    Build parameters.
    
    Args:
        hemi: Hemisphere (e.g., 'lh' or 'rh').
        surface_name: Surface name (e.g., 'white', 'pial').
        subjects: List of subjects to be averaged.
        output_name: Output name for the template.
        addframe_parameters: Add a frame with specific field and location in\
            atlas.
        vector: Print additional information for addframe.
        norot: Not aligning hemispheres before averaging (default).
        rot: Rough rigid alignment of hemispheres before averaging.
        annot: Zero medial wall.
        overlay_parameters: Read overlay from file, specify number of averages.
        overlay_dir: Use directory for overlay hemi.
        scale: Scale value for transformation.
        surf_dir: Use custom subdirectory instead of 'surf'.
        smooth_iterations: Number of iterations to smooth curvature.
        subjects_dir: Specify SUBJECTS_DIR.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_make_template",
        "hemi": hemi,
        "surface_name": surface_name,
        "subjects": subjects,
        "output_name": output_name,
        "vector": vector,
        "norot": norot,
        "rot": rot,
        "annot": annot,
    }
    if addframe_parameters is not None:
        params["addframe_parameters"] = addframe_parameters
    if overlay_parameters is not None:
        params["overlay_parameters"] = overlay_parameters
    if overlay_dir is not None:
        params["overlay_dir"] = overlay_dir
    if scale is not None:
        params["scale"] = scale
    if surf_dir is not None:
        params["surf_dir"] = surf_dir
    if smooth_iterations is not None:
        params["smooth_iterations"] = smooth_iterations
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    return params


def mris_make_template_cargs(
    params: MrisMakeTemplateParameters,
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
    cargs.append("mris_make_template")
    cargs.append(params.get("hemi"))
    cargs.append(params.get("surface_name"))
    cargs.extend(params.get("subjects"))
    cargs.append(params.get("output_name"))
    if params.get("addframe_parameters") is not None:
        cargs.extend([
            "-addframe",
            *params.get("addframe_parameters")
        ])
    if params.get("vector"):
        cargs.append("-vector")
    if params.get("norot"):
        cargs.append("-norot")
    if params.get("rot"):
        cargs.append("-rot")
    if params.get("annot"):
        cargs.append("-annot")
    if params.get("overlay_parameters") is not None:
        cargs.extend([
            "-overlay",
            *params.get("overlay_parameters")
        ])
    if params.get("overlay_dir") is not None:
        cargs.extend([
            "-overlay-dir",
            params.get("overlay_dir")
        ])
    if params.get("scale") is not None:
        cargs.extend([
            "-s",
            str(params.get("scale"))
        ])
    if params.get("surf_dir") is not None:
        cargs.extend([
            "-surf_dir",
            params.get("surf_dir")
        ])
    if params.get("smooth_iterations") is not None:
        cargs.extend([
            "-a",
            str(params.get("smooth_iterations"))
        ])
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "-sdir",
            params.get("subjects_dir")
        ])
    return cargs


def mris_make_template_outputs(
    params: MrisMakeTemplateParameters,
    execution: Execution,
) -> MrisMakeTemplateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisMakeTemplateOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_make_template_execute(
    params: MrisMakeTemplateParameters,
    execution: Execution,
) -> MrisMakeTemplateOutputs:
    """
    This program will add a template into an average surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisMakeTemplateOutputs`).
    """
    params = execution.params(params)
    cargs = mris_make_template_cargs(params, execution)
    ret = mris_make_template_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_make_template(
    hemi: str,
    surface_name: str,
    subjects: list[str],
    output_name: str,
    addframe_parameters: list[str] | None = None,
    vector: bool = False,
    norot: bool = False,
    rot: bool = False,
    annot: bool = False,
    overlay_parameters: list[str] | None = None,
    overlay_dir: str | None = None,
    scale: float | None = None,
    surf_dir: str | None = None,
    smooth_iterations: float | None = None,
    subjects_dir: str | None = None,
    runner: Runner | None = None,
) -> MrisMakeTemplateOutputs:
    """
    This program will add a template into an average surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        hemi: Hemisphere (e.g., 'lh' or 'rh').
        surface_name: Surface name (e.g., 'white', 'pial').
        subjects: List of subjects to be averaged.
        output_name: Output name for the template.
        addframe_parameters: Add a frame with specific field and location in\
            atlas.
        vector: Print additional information for addframe.
        norot: Not aligning hemispheres before averaging (default).
        rot: Rough rigid alignment of hemispheres before averaging.
        annot: Zero medial wall.
        overlay_parameters: Read overlay from file, specify number of averages.
        overlay_dir: Use directory for overlay hemi.
        scale: Scale value for transformation.
        surf_dir: Use custom subdirectory instead of 'surf'.
        smooth_iterations: Number of iterations to smooth curvature.
        subjects_dir: Specify SUBJECTS_DIR.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisMakeTemplateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_MAKE_TEMPLATE_METADATA)
    params = mris_make_template_params(
        hemi=hemi,
        surface_name=surface_name,
        subjects=subjects,
        output_name=output_name,
        addframe_parameters=addframe_parameters,
        vector=vector,
        norot=norot,
        rot=rot,
        annot=annot,
        overlay_parameters=overlay_parameters,
        overlay_dir=overlay_dir,
        scale=scale,
        surf_dir=surf_dir,
        smooth_iterations=smooth_iterations,
        subjects_dir=subjects_dir,
    )
    return mris_make_template_execute(params, execution)


__all__ = [
    "MRIS_MAKE_TEMPLATE_METADATA",
    "MrisMakeTemplateOutputs",
    "MrisMakeTemplateParameters",
    "mris_make_template",
    "mris_make_template_params",
]
